import json


def load() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return  candidates


    def _format_condidates():
        """Форматирование списка кондидатов"""
        candidates: list[dict] = load.json()
        result = '<pre>'

        for candidate in candidates:
            result += f"""
                    {candidate["name"]}\n
                    {candidate["position"]}\n
                    {candidate["skills"]}\n
                """
        result += '<pre>'
        return result

def get_all_condidates() -> list[dict]:
    return  load.json()


def get_condidate_by_id(uid: int) -> dict | None:
    candidates = get_all_condidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None


def get_condidate_by_skill(skill: str) -> list[dict]:
    candidates = get_all_condidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return None
