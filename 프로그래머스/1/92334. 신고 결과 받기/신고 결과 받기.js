function solution(id_list, report, k) {
    let reports = [...new Set(report)].map(r => r.split(' '));
    let reported = new Map();
    for (const report of reports) {
        reported.set(report[1], reported.get(report[1]) + 1 || 1);
    }
    
    let reporter = new Map();
    for (const report of reports) {
        if (reported.get(report[1]) >= k) {
            reporter.set(report[0], reporter.get(report[0]) + 1 || 1);
        }
    }
    
    let answer = id_list.map(r => reporter.get(r) || 0);
    
    return answer;
}