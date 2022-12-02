from flask import Flask


app = Flask(__name__)



@app.route('/')
def page_main():
    """Главная страница"""
    candidates: list[dict] = get_all_condidates()
    result: str = format_candidates(candidates)
    return result



@app.route('/condidate/<int:uid>')
def page_condidate(uid):
    """поиск кондидата по id"""
    candidates: dict = get_candidate_by_id(uid)
    result = f'<img src>="{candidate["pictures"]}">'
    result += format_candidates([candidate])
    return result

@app.route('/skills/<int:skill>')
def page_skills(skill):
    """поиск по навыку"""
    skill_lower = skill.lower
    candidates: list[dict] = get_candidate_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result

app.run



