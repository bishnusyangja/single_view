from django.utils import timezone

from api.helpers import get_random_string
from api.models import MusicalWork
from app.log import get_logger

logger = get_logger()


def reconcile_file(file):
    rows = read_file_content(file)
    save_bulk_obj(rows)


def obj_params_count(obj):
    count = 0
    for field in ('title', 'contributers', 'iswc', 'source', 'item_id',):
        if getattr(obj, field, ''):
            count += 1
    return count


def get_db_iswc_list():
    # we can keep them in redis
    return list(MusicalWork.objects.all().values_list('iswc').order_by('-iswc'))


def get_iswc_index(headers):
    try:
        idx = headers.index('iswc')
    except ValueError:
        idx = -1
    except Exception as exc:
        print('IndexExcep', exc)
        idx = -1
    return idx


def read_file_content(file):
    logger.info("at read file content")
    lines = file.readlines()
    rows = {}
    idx = -1
    headers = []
    batch = get_random_string()
    created_on = timezone.now()
    db_iswc = get_db_iswc_list()
    for i, item in enumerate(lines):
        values = item.decode('utf-8').strip('\n').split(',')
        if i == 0:
            headers = [item.lower().strip() for item in values]
            idx = get_iswc_index(headers)
        else:
            if idx == -1:
                break
            key_item = values[idx] # iswc value for that row
            if key_item and key_item not in db_iswc: # checking the iswc key with database entry
                params = {f'item_{header}' if header == 'id' else header: values[j]
                          for j, header in enumerate(headers) if values[j]}
                params.update(dict(created_on=created_on, batch=batch))
                if key_item in rows:
                    obj = rows[key_item]
                    old_count = obj_params_count(obj)
                    new_count = len(params.keys())
                    if new_count > old_count:
                        obj = MusicalWork(**params)
                        rows[key_item] = obj
                else:
                    obj = MusicalWork(**params)
                    rows[key_item] = obj
    return rows


def save_bulk_obj(rows):
    bulk_obj = rows.values()
    MusicalWork.objects.bulk_create(bulk_obj)
