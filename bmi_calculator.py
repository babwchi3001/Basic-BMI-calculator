class Person:
    def __init__(self, gewicht, grosse, taillenumfang,huftumfang,geschlecht):
        self.gewicht = gewicht
        self.grosse = grosse
        self.taillenumfang = taillenumfang
        self.huftumfang = huftumfang
        self.geschlecht = geschlecht
        
def inp_personal_data():
    gewicht = int
    grosse = int
    taillenumfang = int
    huftumfang = int
    geschlecht = int
    print("Bitte geben Sie Ihr Gewicht ein (in kg): ")
    gewicht = int(input())
    print("Bitte geben Sie Ihre Größe ein (in cm): ")
    große = int(input())
    print("Bitte geben Sie Ihren Taillenumfang ein (in cm): ")
    taillenumfang = int(input())
    print("Bitte geben Sie Ihren Hüftumfang ein (in cm): ")
    huftumfang = int(input())
    print("Geschlecht: (0) Weiblich (1) Männlich: ")
    geschlecht = int(input())
    person = Person(gewicht,große,taillenumfang,huftumfang,geschlecht)
    return person

def comp_bmi(weight, height):
    height = height/100
    height = height*height
    return weight/height
    
def comp_waist_hip(waist, hip):
    return waist/hip
    
def comp_waist_height(waist, height):
    return waist/height
    
def print_results(bmi, waist_hip, waist_height, gen):
    
    print("Ihre Ergebnisse:")
    print("----------------")
    print("Body-Mass-Index: ")
    print(bmi)
    print("Waist-Hip-Ratio: ")
    print(waist_hip)
    print("Waist-Height-Ratio: ")
    print(waist_height)
    print("Ihre Risikofaktoren:")
    print("--------------------")
    
    if(bmi<19):
        print("gem. Body-Mass-Index: Untergewicht")
    elif(19<=bmi<25):
        print("gem. Body-Mass-Index: Normalgewicht")
    elif(25<=bmi<30):
        print("gem. Body-Mass-Index: Übergewicht")
    elif(bmi>=30):
        print("gem. Body-Mass-Index: starkes Übergewicht")
        
    if(gen == 0 and waist_hip <= 0.85*bmi):
        print("gem. Waist-Hip-Ratio: Normalgewicht")
    elif(gen == 0 and waist_hip > 0.85*bmi):
        print("gem. Waist-Hip-Ratio: Übergewicht")
    elif(gen == 1 and waist_hip <= 1):
        print("gem. Waist-Hip-Ratio: Normalgewicht")
    elif(gen == 1 and waist_hip > 1):
        print("gem. Waist-Hip-Ratio: Übergewicht")
        
    if(waist_height < 0.4):
        print("gem. Waist-Height-Ratio: Untergewicht")
    elif(0.4<=waist_height<0.5):
        print("gem. Waist-Height-Ratio: Normalgewicht")
    elif(0.5<=waist_height<0.57):
        print("gem. Waist-Height-Ratio: ̈Ubergewicht")
    elif(waist_height>0.57):
        print("gem. Waist-Height-Ratio: starkes ̈Ubergewicht")
    
    

def main():
    loop_val = 1
    while(loop_val):
        person = inp_personal_data()
        bmi = comp_bmi(person.gewicht,person.grosse)
        hip_waist_ratio = comp_waist_hip(person.taillenumfang, person.huftumfang)
        waist_height_ratio = comp_waist_height(person.taillenumfang,person.grosse)
        print_results(bmi,hip_waist_ratio,waist_height_ratio,person.geschlecht)
        print("Wollen Sie noch weitere Werte berechnen?"
                "(1) Ja"
                "(0) Nein: 0")
        decision = int(input())
        if(not decision):
            loop_val = 0


if __name__ == "__main__":
    main()




