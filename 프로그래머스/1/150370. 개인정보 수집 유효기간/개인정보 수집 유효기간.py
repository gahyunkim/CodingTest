def solution(today, terms, privacies):
    
    def date_to_days(date):
        year, month, day = map(int, date.split('.'))
        return year * 12 * 28 + month * 28 + day

    term_dict = {}
    for term in terms:
        term_type, term_duration = term.split()
        term_dict[term_type] = int(term_duration) * 28 


    today_days = date_to_days(today)
    
    answer = []

    for i, privacy in enumerate(privacies):
        privacy_date, privacy_term = privacy.split()
        privacy_days = date_to_days(privacy_date) 
        expiration_date = privacy_days + term_dict[privacy_term] 

        if today_days >= expiration_date:
            answer.append(i + 1) 
            
    return answer
