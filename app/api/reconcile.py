from api.models import MusicalWork


def obj_params_count(obj):
    count = 0
    for field in ('title', 'contributers', 'iswc', 'source', 'item_id',):
        if getattr(obj, field, ''):
            count += 1
    return count


def reconcile_file(file):
    rows = read_file_content(file)
    save_bulk_obj(rows)


def read_file_content(file):
    lines = file.readlines()
    rows = {}
    idx = -1
    headers = []
    for i, item in enumerate(lines):
        values = item.decode('utf-8').strip('\n').split(',')
        if i == 0:
            headers = [item.lower().strip() for item in values]
            try:
                idx = headers.index('iswc')
            except ValueError:
                idx = -1
            except Exception as exc:
                print('IndexExcep', exc)
                idx = -1
        else:
            if idx == -1:
                break
            key_item = values[idx]
            if key_item and key_item in rows:
                obj = rows[key_item]
                old_count = obj_params_count(obj)
                params = {f'item_{header}' if header == 'id' else header : values[j]
                                                for j, header in enumerate(headers) if values[j]}
                new_count = len(params.keys())
                if new_count > old_count:
                    obj = MusicalWork(**params)
                    rows[key_item] = obj
    return rows


def save_bulk_obj(rows):
    bulk_obj = rows.values()
    MusicalWork.objects.bulk_create(bulk_obj)