style fragments_style:
    xalign 0.5
    yalign 0.9
    spacing 5

init python:
    def arrange_sentence(arranged_sentence,fragment):
        if fragment in arranged_sentence:
            arranged_sentence = arranged_sentence.remove(fragment)
        else:
            arranged_sentence = arranged_sentence.append(fragment)
        return arranged_sentence
        
    def show_sentence(arranged_sentence):
        if arranged_sentence == []:
            sentence = ""
        else: 
            sentence = ' '.join(arranged_sentence)
            #sentence = arranged_sentence[0]
            #for i in range(1,len(arranged_sentence)):
                #sentence += arranged_sentence[i]
        return sentence

screen show_sentence:
    text "[sentence]" xalign 0.2 yalign 0.70 color "#f00" 
    text "[arranged_sentence]" xalign 0.2 yalign 0.65 color "#f00"
    $ l = len(arranged_sentence)
    text "[l]" xalign 0.2 yalign 0.6 color "#f00"
    text "[test]" xalign 0.1 yalign 0.75 color "#f00" 
    #if len(arranged_sentence) > 0:
        #$ testing = arranged_sentence[0]
        #text "[testing]" xalign 0.2 yalign 0.60 color "#f00"
    
screen arrange_screen(fragments,correct_sentence,arranged_sentence,sentence,test):                                                                                                                                             
    text "[test]" xalign 0.2 yalign 0.75 color "#f00" 
    text "[sentence]" xalign 0.2 yalign 0.75 color "#f00" 
    hbox:
        style "fragments_style"
        spacing 10
        xmaximum 300
        for fragment in fragments:
            textbutton fragment:
                #clicked [SetVariable("arranged_sentence",arrange_sentence(arranged_sentence,fragment)),SetVariable("sentence",show_sentence(arranged_sentence))]
                        #action Null
                clicked [SetVariable("arranged_sentence",arrange_sentence(arranged_sentence,fragment)),SetVariable("sentence",show_sentence(arranged_sentence)),SetVariable("test",fragment)]
                #clicked SetVariable("arranged_sentence",arrange_sentence(arranged_sentence,fragment))
                #action SetVariable("sentence",show_sentence(arranged_sentence))
                #clicked SetVariable("sentence",fragment)
                #clicked [AddToSet("arranged_sentence",fragment),SetVariable("sentence",show_sentence(arranged_sentence))]
                text_size 24
        #textbutton "我"
            #clicked [SetVariable("arranged_sentence",arrange_sentence(arranged_sentence,"我")),SetVariable("sentence",show_sentence(arranged_sentence)),SetVariable("test","我")]
        #textbutton "可不可以"
            #clicked [SetVariable("arranged_sentence",arrange_sentence(arranged_sentence,"可不可以")),SetVariable("sentence",show_sentence(arranged_sentence)),SetVariable("test","可不可以")]
        #textbutton "以后"
             #clicked [SetVariable("arranged_sentence",arrange_sentence(arranged_sentence,"以后")),SetVariable("sentence",show_sentence(arranged_sentence)),SetVariable("test","以后")]
        
                    