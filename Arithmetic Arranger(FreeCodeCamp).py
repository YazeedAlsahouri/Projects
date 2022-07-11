def Check_if(n):
    for i in n:
        for j in i.split():
            if j!="+" and j!="-":
                if not j.isdigit():
                    return False
    return True
def arithmetic_arranger(problems,option=False):
    if len(problems)<=5:
        for i in problems:
            k=i.split()
            if "+" in k or "-" in k:
                flag=Check_if(i)
                if flag:
                    if len([z for z in k[0] if z.isdigit()])<=4 and len([y for y in k[-1] if y.isdigit()])<=4:
                        if option=="Yes":
                            if k[1]=="+":
                                result=int(k[0])+int(k[-1])
                            else:
                                result=int(k[0])-int(k[-1])
                            print(f"""  {k[0]}
{k[1]} {k[-1]}
----                                  
 {result}
---------------""")
                        else:
                            print(f"""  {k[0]}
{k[1]} {k[-1]}
----
---------------""")
                            
                    else:
                        return "Numbers cannot be more than four digits."
                else:
                    return "Operator must be '+' or '-'."
            else:
                return"Operator must be (+) or (-)"
    else:
        return "Too many problems."
my_list=[]
count_problems=int(input("Enter how many arithmetic problems do you want to solve: "))
for count in range(count_problems):
    problem=input(f"Enter your arithmetic problem number {count+1}: ")
    if " + " in problem or " - " in problem:  
        my_list.append(problem)
    elif "+ " in problem or "- " in problem:
        if "+" in problem:
            problem=problem.replace("+"," +")
            my_list.append(problem)
        elif "-" in problem:
            problem=problem.replace("-"," -")
            my_list.append(problem)
    elif " +" in problem or " -" in problem:
        if "+" in problem:
            problem=problem.replace("+","+ ")
            my_list.append(problem)
        elif "-" in problem:
            problem=problem.replace("-","- ")
            my_list.append(problem)
    elif not " " in problem:
        if "+" in problem:
            problem=problem.replace("+"," + ")
            my_list.append(problem)
        elif "-" in problem:
            problem=problem.replace("-"," - ")
            my_list.append(problem)
option=bool(input("if you want to show the solution of problems Enter (Yes) if you dont want Enter (No): ").capitalize())
print(arithmetic_arranger(my_list,option))
