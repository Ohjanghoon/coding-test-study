def solution(id_list, report, k):
    answer = []
    
    report_dict = {}
    
    for i, user_id in enumerate(id_list):
        answer.append(0)
        report_dict[user_id] = {"report": set([]), "receive": set([])}
    
    # print(report_dict)
    
    for r in report:
        user_id, report_id = r.split(' ')
        report_dict[report_id]["receive"].add(user_id)
        report_dict[user_id]["report"].add(report_id)
        
    for idx, key in enumerate(report_dict.keys()):
        report_ids = list(report_dict[key]["report"])
        
        for ri in report_ids:
            if len(report_dict[ri]["receive"]) >= k:
                answer[idx] += 1
        
    return answer