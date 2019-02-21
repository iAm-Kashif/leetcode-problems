"""
811. Subdomain Visit Count
https://leetcode.com/problems/subdomain-visit-count/

_author:            Kashif Memon
_python_version:    3.7.2
"""


def run_solution(cpdomains: 'List[str]') -> 'List[str]':
    all_domains = {}
    out = []

    for item in cpdomains:
        count, domain = item.split(" ")
        for i in range(len(domain)):

            if domain in all_domains.keys():
                all_domains[domain] = int(all_domains[domain]) + int(count)
            else:
                all_domains[domain] = count

            i = domain.find(".")
            if i == -1:
                break
            domain = domain[i+1:]
    for key, value in all_domains.items():
        out.append(str(value) + " " + key)
    return out





def main():
    input1 = ["9001 discuss.leetcode.com"]
    input2 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    # run_solution(input1)
    run_solution(input2)


if __name__ == "__main__":
    main()