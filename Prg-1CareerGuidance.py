print("---------------------------------------------------------")
print("            CAREER GUIDANCE SYSTEM            ")
print("---------------------------------------------------------")
print("Answer the following questions in Yes or No.")
print("\n")

coding = input("Do you like coding? ").lower()
math = input("Do you like mathematics? ").lower()
biology = input("Do you like biology? ").lower()
drawing = input("Do you like drawing? ").lower()

print("\n")
print("---------------Career Suggestion---------------")

if coding=="no" and math=="no" and biology=="no" and drawing=="no":
    print("Explore your interest and career option further...")
    
elif coding=="no" and math=="no" and biology=="no" and drawing=="yes":
    print("Suggested Career : Graphic Designer/Animator")
    
elif coding=="no" and math=="no" and biology=="yes" and drawing=="no":
    print("Suggested Career : Pharmacist/Nurse")
    
elif coding=="no" and math=="no" and biology=="yes" and drawing=="yes":
    print("Suggested Career : Medical Illustrator/Healthcare Educator")
    
elif coding=="no" and math=="yes" and biology=="no" and drawing=="no":
    print("Suggested Career : Engineer/Data Analyst")
    
elif coding=="no" and math=="yes" and biology=="no" and drawing=="yes":
    print("Suggested Career : Architect")

elif coding=="no" and math=="yes" and biology=="yes" and drawing=="no":
    print("Suggested Career : Doctor")
    
elif coding=="no" and math=="yes" and biology=="yes" and drawing=="yes":
    print("Suggested Career : Medical Illustrator/Biomedical Designer")

elif coding=="yes" and math=="no" and biology=="no" and drawing=="no":
    print("Suggested Career : Programmer/Web Developer")

elif coding=="yes" and math=="no" and biology=="no" and drawing=="yes":
    print("Suggested Career : Web Designer/UI-UX Designer")

elif coding=="yes" and math=="no" and biology=="yes" and drawing=="no":
    print("Suggested Career : Health App Developer")

elif coding=="yes" and math=="no" and biology=="yes" and drawing=="yes":
    print("Suggested Career : Medical Illustrator")

elif coding=="yes" and math=="yes" and biology=="no" and drawing=="no":
    print("Suggested Career : Software Engineer/Computer Scientist")

elif coding=="yes" and math=="yes" and biology=="no" and drawing=="yes":
    print("Suggested Career : Game Developer/UI Engineer")

elif coding=="yes" and math=="yes" and biology=="yes" and drawing=="no":
    print("Suggested Career : Bioinformation Scientist")

elif coding=="yes" and math=="yes" and biology=="yes" and drawing=="yes":
    print("Suggested Career : Biomedical Software Engineer/Medical Technology Specialist")
    
else:
    print("Explore general management, arts, or commerce fields to find your passion!")

print("Thanks for using Career Suggestion boat!!^_^")
