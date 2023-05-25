from django.shortcuts import HttpResponse,render

def test(request):
    name = "Rahul Dravid"
    profession = "coach"
    return render(request, "test.html", {"name": name, "profession": profession})

def quiz(request):
    questions = [('1-Varanasi located in ..','a-Varanasi','b-gazipur','c-Jounpur','d-Allahabad',1),
                ('2-Uttar Pradesh stands for .. ','a-MP','b-CG','c-UP','d-HP',3),
                 ('3-Rishikesh in  .. ','a-UP','b-CG','c-UP','d-UK',4)]
    question=""
    x = 0
    if request.GET:
        x=request.GET['question']
        x=int(x)+1
        if x>=len(questions):
            return HttpResponse('testOver')
    question = questions[x]
    return render(request, 'newq.html',
                  {"qno": x,"currentquestion":question[0],"opta":question[1],"optb":question[2],"optc":question[3],"optd":question[4]})

def question(request):
    questions = [('(1)- Python was developed by Guido van Rossum', 1),
                 ('(2)- Python is case sensitive', 1),
                 ('(3)- Python is good for health', 0),
                 ('(4)- The blue whale is the biggest animal to have ever lived.', 1),
                 ('(5)- Python is full stack ?', 1)]
    x = 0
    previousquestion = ""
    result = ""
    option = ""
    score = 0
    n = len(questions)
    if request.GET:
        x = request.GET['question']
        option = int(request.GET['option'])
        score = request.GET['score']
        x = int(x)
        score = int(score)
        previousans = questions[x][1]
        previousquestion = questions[x][0]
        if option == previousans:
            result = "Correct"
            score = score + 1
        else:
            result = "Wrong"
        x = x + 1
        print(result, "option=", option, "ans=", previousans, score)
        if x >= n:
            # return HttpResponse('Test Over--Yur score is --' + str(score))
            return render(request, 't.html', {'result': result, 'score': score})

    questions = questions[x][0]
    return render(request, "q.html",
                  {"qno": x, 'currentquestion': questions, 'result': result, 'previousans': previousquestion,"score": score})
