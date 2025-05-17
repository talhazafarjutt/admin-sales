def apply_pagination(query, skip: int, limit: int):
    return query.offset(skip).limit(limit)