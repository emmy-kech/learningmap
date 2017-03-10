skills = {}
while True:
    k = raw_input("add skills: ")
    val = raw_input("have you done this skill? Write yes or no: ") #this indicates the skills i have studied
    skills[k] = val
    skills.update({k:val})
    print('my skills: ',k) #this lists all the skills

#this displays my learning progress
    if len(skills) > 3:
        if val == 'yes':
            print('skills studies: ', k)  # this lists the skills studied
        if val == 'no':
            print('skill not studied: ', k)  # this lists the skills i have not studied
        print ('This is my learning progress: ', skills)



