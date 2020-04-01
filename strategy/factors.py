"""
helper functions
"""


def between(attr, min, max, view=False):
    if view:
        return {'view_between_%s' % attr: (min, max)}
    else:
        return {'filter_between_%s' % attr: (min, max)}


def isin(attr, list, view=False):
    if view:
        return {'view_isin_%s' % attr: tuple(list)}
    else:
        return {'filter_isin_%s' % attr: tuple(list)}


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    - normally some combination of make_criteria_between() and make_criteria_isin()
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def apply_criteria(df, dict_crit):
    for param, vals in dict_crit.items():
        apply_type = param.split('_')[0]  # 'filter' or 'view'
        attr = '_'.join(param.split('_')[2:])  # target column name
        filter_type = param.split('_')[1]  # 'isin' or 'between'
        if apply_type == 'filter':
            if filter_type == 'between':
                df = df[df[attr].between(vals[0], vals[1])]
            elif filter_type == 'isin':
                df = df[df[attr].isin(vals)]
        elif apply_type == 'view':
            if filter_type == 'between':
                df[param] = df[attr].between(vals[0], vals[1]).astype(int)
            elif filter_type == 'isin':
                df[param] = df[attr].isin(vals).astype(int)
    return df
