# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define panda = Character("Panda",color="#cccccc" )
define player=Character("[povname]")
define roommate=Character("Roommate")
define professor=Character("Professor Li")
define vendor=Character("Vendor")
define driver=Character ("Driver")
define taxi = Character("Taxi Driver")
define bankTeller = Character("Bankteller")
define stranger = Character("Stranger")
define friend = Character("Friend")
define ticketAttendant = Character("Ticket Attendant")
define trainAttendant = Character("Train Attendant")
define friend=Character("Friend")
define salesperson=Character("Salesperson")
define waiter=Character("Waiter")
define hotelclerk=Character("Hotel Clerk")

image bg park=im.Scale("Park View Sketch.png",1280,780)
image bg parkbush="Panda in Bush Sketch.png"
image bg office=im.Scale("Professor Office Sketch.png",1280,780)
image university=im.Scale("Peking University Sketch.png",1280,780)
image bg bus= im.Scale("bus unshaded.png",1280,720)
image bg fruit="Fruit Vendor Sketch.png"
image pda stand="panda standing.png"
image bd driverstand="bus driver hello (1).png"
image bg road = im.Scale("Bus _ Taxi Sketch (ROUGH).png", 1280, 780)
image bg insidetaxi = im.Scale("Inside Taxi Sketch.png", 1280, 780)
image bg ATMSketch = im.Scale("ATM Sketch.png", 1280, 780)
image bg outsidebank = im.Scale ("Bank Sketch.png", 1280, 780)
image bg insidebank = im.Scale("Bank Teller Sketch.png", 1280, 780) 
image pda backpack="panda backpack.png"
image bg hotel = im.Scale("Hotel Sketch.png",1280,780)
image bg hotelroom = im.Scale("Hotel Room Sketch.png", 1280,780)
image bg trainStation = im.Scale("Train Station Sketch.png", 1280, 780)
image bg insideTrain = im.Scale("Inside Train Sketch.png",1280,780)
image bg ticketBooth = im.Scale("Train Ticket Booth Sketch.png",1280,780)
image bg clothes store=im.Scale("Mall Clothing Store Sketch.png", 1280, 780)
image bg street = im.Scale("Street in Sichuan Sketch.png", 1280, 780)
image bg panda base = im.Scale("Chengdu Panda Base.png",1280,780)
image bg restaurant=im.Scale("Restaurant Sketch.png", 1280, 780)
image bg restaurant bathroom=im.Scale("Restaurant Bathroom Sketch.png", 1280, 780)
image bg food = "food bg.png"
image pda talk1="panda normal speaking 1"
image pda talk2="panda normal speaking 2"
image pda talk3="panda normal speaking 3"
image pda talk:
    "panda normal speaking 1"
    0.1
    "panda normal speaking 2"
    0.1
    "panda normal speaking 3"
    0.1
    repeat
image pda backpack s=im.Scale("panda backpack.png",400,400, xoffset=500, yoffset=0)
image pda yawn = im.Scale("panda yawn.png",400,400,xoffset=0, yoffset=-45)
image driv standard=im.Scale("bus driver hello (1).png",1280,780)
image driv confused=im.Scale("bus driver confused.png",1280,780)
image driv happy=im.Scale("bus driver happy.png",1280,780)
image prof happy=im.Scale("prof happy.png",600,796, xoffset=0, yoffset=75)
image prof angry=im.Scale("prof angery.png",600,796, xoffset=0, yoffset=75)
image vendor normal=im.Scale("fruit_vendor_normal.png",1280,720)
image vendor angry=im.Scale("fruit_vendor_angry.png",1280,720)
image vendor confused=im.Scale("fruit_vendor_confused.png",1280,720)
image sales normal=im.Scale("store salesperson normal.png", 750, 750, xoffset=0, yoffset=40)
image sales angry=im.Scale("store salesperson angry.png",750, 750, xoffset=0, yoffset=40)
image sales confused=im.Scale("store salesperson confused.png", 750, 750, xoffset=0, yoffset=40)
image text one=im.Scale ("text_friend1.png", 750,750)
image text two=im.Scale ("text_friend2.png", 750,750)
image taxidriver normal= im.Scale ("taxi driver normal.png", 1280,720)
image taxidriver angry=im.Scale("taxi driver angry.png", 1280,720)
image taxidriver confused=im.Scale("taxi driver confused.png", 1280,720)
image bankteller normal=im.Scale("bank teller normal.png", 650, 650, xoffset=0, yoffset=30)
image bankteller angry=im.Scale("bank teller angry.png", 650, 650,xoffset=0, yoffset=30)
image bankteller confused=im.Scale("bank teller confused.png", 650, 650, xoffset=0, yoffset=30)
image ticketattendant normal=im.Scale("ticket attendant normal.png", 1280, 780)
image ticketattendant confused=im.Scale("ticket attendant confused.png", 1280, 780)
image ticketattendant angry=im.Scale("ticket attendant angry.png", 1280, 780)
image trainattendant normal=im.Scale("train attendant normal.png",600,600)
image trainattendant angry=im.Scale("train attendant angry.png",600,600)
image trainattendant confused=im.Scale("train attendant confused.png",600,600)
image hotelclerk confused=im.Scale("hotel clerk confused.png",680,680,xoffset=0, yoffset=48)
image hotelclerk angry=im.Scale("hotel clerk angry.png",680,680,xoffset=0, yoffset=48)
image hotelclerk normal=im.Scale("hotel clerk normal.png",680,680,xoffset=0, yoffset=48)
image friend normal=im.Scale("friend normal.png",1280,720)
image friend angry=im.Scale("friend angry.png",1280,720)
image friend confused=im.Scale("friend confused.png",1280,720)
image waiter normal=im.Scale("waiter normal.png",750,750,xoffset=0, yoffset=60)
image waiter angry=im.Scale("waiter angry.png",750,750,xoffset=0, yoffset=60)
image waiter confused=im.Scale("waiter confused.png",750,750,xoffset=0, yoffset=60)
image restaurant food=im.Scale("Chinese Food Sketch.png",200,200,xoffset=0, yoffset=-5)
image restaurant food zoomin =im.Scale("Chinese Food Sketch.png",800,800)
image stranger normal = im.Scale("stranger normal.png",600,600)
image stranger confused = im.Scale("stranger confuse.png",600,600)
image stranger angry = im.Scale("stranger angry.png",600,600)
image point box = im.Scale("pointbox.png",550,80,xoffset=620, yoffset=-600)

# Screen for displaying points  
define points = 0
define start_time = 0
define elapsed_time = 0
screen Points_display:
     text "[points]" xpos 1180 ypos 0.090 size 35

#Save data initializations
init python:
    from datetime import datetime

#set directory for saving data
define config.savedir = "/Users/yeelissa/Documents/renpy-pandamonium/Pandamonium/savedata/"
define first_officeQ1 = True
define first_officeQ2 = True
define first_officeQ3 = True
define first_officeQ4 = True
define first_fruitQ1 = True
define first_fruitQ2 = True
define first_busQ1 = True
define first_busQ2 = True
define first_taxiQ1 = True
define first_bankQ1 = True
define first_trainQ1 = True
define first_insidetrainQ1 = True
define first_storeQ1 = True
define first_storeQ2 = True
define first_storeQ3 = True
define first_storeQ4 = True 
define first_storeQ5 = True
define first_restaurantQ1 = True
define first_restaurantQ2 = True
define first_restaurantQ3 = True
define first_restaurantQ4 = True
define first_streetQ1 = True
define first_streetQ2 = True
define first_streetQ3 = True


# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $povname = "You"

    scene bg park
    with dissolve
    play music "Deep Chills.mp3"
    "You are an exchange student in Beijing University. You arrived in China a few days ago. One night, you go for a walk in Beihai park."
    scene bg parkbush 
    with dissolve
    
   
    "You see a panda in the bush. You walk closer."
    "The panda seems lost. Suddenly, the panda begins talking to you."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show pda talk at Position (xpos=0.46, xanchor=0.46)
    with dissolve
    

    # These display lines of dialogue.
    
    panda "Hey, human, what are you looking at?"
    show pda talk2
    with dissolve
    player "A talking panda?!"
    show pda talk
    with dissolve
    panda "What, you haven't seen a talking panda before?"
    show pda talk2
    with dissolve
    player "Well, not really. What are you doing here?"
    show pda talk
    with dissolve
    panda "Shhh, some evil humans kidnapped me. I managed to escape and now I’m hiding from them. I need to find my way back home. Can you help me?"
    show pda talk2
    with dissolve
    player "Sure. But I'm an exchange student. My Chinese isn't good enough to get around..."
    show pda talk
    with dissolve
    panda "That's ok. I can teach you, if you bring me back home." 
    show pda talk2
    with dissolve
    player "If you say so, I guess let's go?"
    show pda talk
    with dissolve
    panda "Wait one second kid,"
    show pda talk2
    with dissolve
    $povname=renpy.input("你叫什么名字?")
    $povname=povname.strip()
    $ filename = povname + ".txt"
    $ f = open(config.savedir + filename, 'a+')
    $ f.write('username: ' + povname + "\n")
    panda "你好，我叫包包。"


    scene bg parkbush

    show text one
    with dissolve

    player "Hey, I just met a lost panda. I think I will try to bring him home to Sichuan."

    hide text one
    show text two
    with dissolve
    roommate "OMG! I wish I could go with you. Are you going to miss classes?"

    hide text two
    show text one
    with dissolve
    player "Yes, I'm going to talk to Professor Li tomorrow morning." 


    scene university
    with dissolve
    show point box onlayer screens
    show screen Points_display 
    show pda backpack
    with dissolve
    "The next day, you put the panda in your backpack and walk to the office building in your university."
    scene bg office
    show prof happy
    with dissolve
    professor "请进。" 
    player "李老师，您好。"
  
    label officeQ1:
        if first_officeQ1:
            $ f.write('officeQ1: ')
            #$ renpy.clear_game_runtime() 
            $ first_officeQ1 = False
        hide pda backpack s onlayer top 
        show prof happy
        professor "你好。请坐，有事吗？"
        player "李老师，不好意思，我家有点急事。"
    
    menu oq1:
        "我得有一个假期，好不好？":
            jump socioOffice1
        "我可以请假几天呢？":
            jump grammarOffice1
        "我想有几天不参加上课。":
            jump conventionalOffice1
        "我可以请几天假吗？":
            jump rightOffice1
            
    label socioOffice1:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top 
        with dissolve
        panda "得 might be too demanding here. Think about the context."
        jump officeQ1
        
    label grammarOffice1:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top 
        with dissolve
        panda "呢 is grammatically incorrect here."
        jump officeQ1
    
    label conventionalOffice1:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top 
        with dissolve
        panda "不参加上课 is not the way Chinese people would say it."
        jump officeQ1
    
    label rightOffice1:
        #$ elapsed_time = renpy.get_game_runtime() 
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        #$ f.write(str(points) + str(elapsed_time) + "\n")
        play sound "right.mp3"
        show prof happy
        professor "嗯，好吧。"
        jump fillblankOffice1 #officeQ2
    
    label fillblankOffice1:
        show pda backpack s onlayer top 
        with dissolve
        panda "Now try recalling what you just learned. Fill in the missing sentence fragment."
        $answer=renpy.input("我可以___吗？")
        $answer=answer.strip()
        if answer == "请几天假":
            jump fillblackOffice1_right
        else:
            jump fillblackOffice1_wrong
    
    label fillblackOffice1_right:
        play sound "right.mp3"
        panda "Correct!"
        jump officeQ2
    
    label fillblackOffice1_wrong:
        play sound "wrong.wav"
        panda "Wrong. Try Again."
        jump fillblankOffice1
        
    label officeQ2:
        if first_officeQ2:
            $ f.write('officeQ2: ')
            $ renpy.clear_game_runtime() 
            $ first_officeQ2 = False
        show prof happy
        hide pda backpack s onlayer top 
        professor "不过你会错过明天的考试哦。"
    
    menu oq2:

        "我回来以后补考怎么样？":
            jump socioOffice2
        "我可不可以回来以后补考吗？":
            jump grammarOffice2
        "我可不可以回来以后补考呢?":
            jump rightOffice2
        "我回来以后再考一次，好不好？":
            jump conventionalOffice2
    
    label conventionalOffice2:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "再考一次 is not the conventional way to say it."
        jump officeQ2
        
    label grammarOffice2:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show prof angry
        professor "......"
        show pda backpack s onlayer top
        with dissolve
        panda "吗 is redundant."
        jump officeQ2
    
    label socioOffice2:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "怎么样 is used to make suggestions. Think about the situation here."
        jump officeQ2
    
    label rightOffice2:
        #$ elapsed_time2 = renpy.get_game_runtime() 
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        #$ f.write(str(points) + str(elapsed_time2) + "\n")
        play sound "right.mp3"
        show prof happy
        hide pda backpack s onlayer top
        #professor "好的，那下星期回来以后补考吧。"
        jump officeQ3
        #jump arrangeOffice2
        
    #label arrangeOffice2:
        #$ message = "Testing this out."
        #yes_action = jump officeQ3
        #no_action = jump arrangeOffice2
        #show screen confirm(message, yes_action, no_action)
        #$ test="a"
        #$ fragments=["我","可不可以","回来","以后","补考","呢","?"]
        #$ fragments=["hi","how","are","you","?"]
        #$ correct_sentence="我可不可以回来以后补考呢?"
        #$ arranged_sentence = []
        #$ sentence = ""
        #show screen show_sentence
        #call screen arrange_screen(fragments,correct_sentence,arranged_sentence,sentence,test) 
        
    label officeQ3:
        hide pda backpack s onlayer top
        if first_officeQ3:
            $ f.write('officeQ3: ')
            $ first_officeQ3 = False
        show prof happy
        professor "好的，那下星期回来以后补考吧。"
        
    menu moq3:
        "太好了！谢谢老师。":
            jump rightOffice3
        "太好了！谢了啊！":
            jump socioOffice3
        "太好了！很谢谢您了！":
            jump grammarOffice3
        "多谢！多谢啊！":
            jump conventionalOffice3
        
    label socioOffice3:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "谢了啊 is too informal. Think about the context."
        jump officeQ3
        
    label grammarOffice3:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "We don't say 很......了."
        jump officeQ3
        
    label conventionalOffice3:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "That's not the way Chinese people would say it."
        jump officeQ3
    
    label rightOffice3:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        show prof happy
        hide pda backpack s onlayer top
        professor "不客气。还有别的事吗？"
        jump officeQ4

    label officeQ4:
        hide pda backpack s onlayer top
        if first_officeQ4:
            $ f.write('officeQ4: ')
            $ first_officeQ4 = False
        show prof happy
        player "没事了，谢谢老师。"
        
    menu moq4:

        "我要离开了！再见！":
            jump socioOffice4
        "那我先走了。再见！":
            jump rightOffice4
        "那我出去。再见！":
            jump grammarOffice4
        "我要走。再见！":
            jump conventionalOffice4
            
    label socioOffice4:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show prof angry
        with dissolve
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "离开 (to leave/depart) is too formal here. "
        jump officeQ4
    
    label grammarOffice4:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show prof angry
        with dissolve
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "出去 means going out."
        jump officeQ4
    
    label conventionalOffice4:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show prof angry
        with dissolve
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "我要走 is not the conventional way to say it. "
        jump officeQ4
        
    label rightOffice4:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        show prof happy
        professor "好，再见！"
        
    "After you meet with your professor, you walk out of the university. Suddenly, you hear the panda crying."
    scene university
    show pda yawn
    with dissolve
    player "Are you okay, buddy?"
    hide pda yawn
    with dissolve
    show pda talk2
    with dissolve
    panda "Do I look okay to you?"
    show pda talk
    show pda talk2
    player "Sorry... I was just asking..."
    show pda talk
    panda "Well, it's just...I haven't gotten to eat in a long time. I'm so hungry."
    show pda talk2
    player "I can get you food! What do you want? There's a fruit vendor right over there!"
    show pda talk
    panda "You know, bamboo is my favorite. But I'm starving now. Apples will do."
    
    scene bg fruit
    
    label fvq1:
        hide pda backpack s onlayer top
        show vendor normal
        with dissolve
        if first_fruitQ1:
            $ f.write('fruitQ1: ')
            $ first_fruitQ1 = False
        vendor "买点苹果吗？"
    
    menu mfvq1:
        
        "苹果值多少钱？":
            jump sociofruit1
        "苹果多少钱？":
            jump rightfruit1
        "苹果多少？":
            jump grammarfruit1
        "一个苹果几块钱？":
            jump conventionalfruit1
            
    label conventionalfruit1:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        hide pda backpack s onlayer top
        hide vendor normal
        hide vendor angry
        show vendor confused
        vendor "......"
        show pda backpack s onlayer top
        with dissolve
        panda "一个 is not the conventional way to ask for the price of fruit in China because fruit is sold by kilos here."
        jump fvq1
    
    label grammarfruit1:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        hide pda backpack s onlayer top
        hide vendor normal
        hide vendor angry
        show vendor confused
        vendor "......"
        show pda backpack s onlayer top
        with dissolve
        panda "钱 is missing here. "
        jump fvq1
    
    label sociofruit1:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        hide pda backpack s onlayer top
        hide vendor normal
        hide vendor confused
        show vendor angry
        vendor "......"
        show pda backpack s onlayer top
        with dissolve
        panda "值 (worth) sounds too formal in this context."
        jump fvq1
            
    label rightfruit1:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        hide vendor angry
        hide vendor confused
        if first_fruitQ2:
            $ f.write('fruitQ2: ')
            $ first_fruitQ2 = False
        show vendor normal
        vendor "六块钱一斤。"
        
    menu fvq2:
        "便宜点吧！":
            jump rightfruit2
        "便宜一下吧！":
            jump grammarfruit2
        "能不能打折？":
            jump sociofruit2
        "不要太贵了。":
            jump conventionalfruit2
    
    label grammarfruit2:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        hide pda backpack s onlayer top
        hide vendor angry
        hide vendor normal
        show vendor confused
        vendor "......"
        show pda backpack s onlayer top
        with dissolve
        panda "一下 doesn't go with 便宜 because 便宜 is an adjective."
        jump fvq2
    
    label sociofruit2:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        hide pda backpack s onlayer top
        hide vendor angry
        hide vendor normal
        show vendor confused
        vendor "......"
        show pda backpack s onlayer top
        with dissolve
        panda "打折 sounds too formal here."
        jump fvq2
    
    label conventionalfruit2:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        hide pda backpack s onlayer top
        hide vendor confused
        hide vendor normal
        show vendor angry 
        vendor "......"
        show pda backpack s onlayer top
        with dissolve
        panda "不要太贵了 is not the way people bargain. "
        jump fvq2

    label rightfruit2:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        hide vendor angry
        hide vendor confused
        show vendor normal
        vendor "最低五块钱。"
        player "好吧，我买两斤。"
        
    show pda backpack s onlayer top
    panda "Give me the food! Now come on we need to catch that bus!"
    scene bg bus
    hide pda backpack s onlayer top
    player "Sheesh, do you really have to be so bossy."
    "You'd think the panda would be more grateful. Anyway, the bus is here. We need to go to the bank to get some money for the trip."

    label bdq1:
        hide bg bus
        hide pda backpack s onlayer top
        if first_busQ1:
            $ f.write('busQ1: ')
            $ first_busQ1 = False
        show driv standard
        with dissolve
        
    menu mbdq1:
        "师傅，我要去中国银行，去不去？":
            jump sociobd1
        "师傅，请问，向中国银行吗？":
            jump grammarbd1
        "师傅，请问，到中国银行吗？":
            jump rightbd1
        "师傅，请问，你的公共汽车去不去中国银行？":
            jump conventionalbd1
            
    label sociobd1:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "要 might be too demanding here. Think about the context/situation. "
        jump bdq1
    
    label grammarbd1:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "向 means towards. Is it correct here?"
        jump bdq1
        
    label conventionalbd1:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "你的公共汽车 is not the conventional way to say it. "
        jump bdq1
            
    label rightbd1:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        if first_busQ2:
            $ f.write('busQ2: ')
            $ first_busQ2 = False
        show driv happy
        with dissolve
        driver "这辆车不到。"
        
    menu bdq2:
        
        "我怎么去中国银行？":
            jump sociobd2
        "那请问哪辆车到中国银行吗？":
            jump grammarbd2
        "那请问哪辆车到中国银行？":
            jump rightbd2
        "那请问什么公共汽车可以去中国银行？":
            jump conventionalbd2
            
    label sociobd2:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "怎么去 sounds a little demanding here. Think about the context/situation."
        jump bdq2
        
    label grammarbd2:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "吗 is redundant here."
        jump bdq2
        
    label conventionalbd2:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "什么公共汽车 is not the conventional way to refer to buses."
        jump bdq2
        
    label rightbd2:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        driver "公交车都不到。你得打车了。"
        
    label janet:
        "Because the bus doesn't go there, you walk out of the bus to wait for a taxi. "
        show bg road
        with dissolve
        
        "A few minutes later, you see a taxi approaching. You hail the taxi driver."
        scene bg insidetaxi
        with dissolve
        "The taxi stops to let you enter and you open the door to enter the taxi."
        

    # These display lines of dialogue.
        scene bg insidetaxi
        
        label taxiQ1:
            hide taxidriver confused
            hide taxidriver angry
            hide pda backpack s onlayer top
            if first_taxiQ1:
                $ f.write('taxiQ1: ')
                $ first_taxiQ1 = False
            show taxidriver normal
            with dissolve
            taxi "你好!"
    
        menu tq1:
            "请问我可不可以去中国银行？":
                jump socioTaxi1
            "到中国银行。":
                jump grammarTaxi1
            "去中国银行怎么样？":
                jump conventionalTaxi1
            "去中国银行。":
                jump rightTaxi1
                
        label socioTaxi1:
            $ points -= 1 
            $ f.write('s')
            play sound "wrong.wav"
            show taxidriver confused
            taxi "......"
            show pda backpack s onlayer top
            with dissolve         
            panda "Is this too elaborate here? Think about the context/situation. "
            jump taxiQ1
            
        label grammarTaxi1:
            $ points -= 1 
            $ f.write('g')
            play sound "wrong.wav"
            show taxidriver angry
            taxi "......"
            show pda backpack s onlayer top
            panda "到 means arrive. "
            jump taxiQ1
            
        label conventionalTaxi1:
            $ points -= 1 
            $ f.write('c')
            play sound "wrong.wav"
            show taxidriver confused
            taxi "......"
            show pda backpack s onlayer top
            panda "怎么样 is not the conventional way to give direction to the taxi driver."
            jump taxiQ1
            
        label rightTaxi1:
            $ points += 3 
            $ f.write('r ')
            $ f.write(str(points) + "\n")
            play sound "right.mp3"
            show taxidriver normal
            with dissolve
            hide pda backpack s onlayer top
            taxi "好咧。"
 
    # The bank scene.
        scene bg outsidebank
        with dissolve 
        "As you get to the bank, you walk onto the ATM machine to withdraw some money for the trip."
        scene bg ATMSketch
        with dissolve
        "But the ATM freezes up and doesn't respond to you! You have to talk to someone."

        label bankQ1:
            show bg insidebank
            hide bankteller angry
            hide bankteller confused
            hide pda backpack s onlayer top
            if first_bankQ1:
                $ f.write('bankQ1: ')
                $ first_bankQ1 = False
            show bankteller normal
            bankTeller "您好，请问您需要办理什么业务?"

        menu bq2:
            "我想拿800块钱。":
                jump socioBank1
            "我想取800块钱。":
                jump rightBank1
            "我想取800块钱吗? ":
                jump grammarBank1
            "拿800块钱怎么样？":
                jump conventionalBank1
                
        label socioBank1:
            $ points -= 1 
            $ f.write('s')
            play sound "wrong.wav"
            hide bankteller normal
            show bankteller angry
            bankTeller "......"
            show pda backpack s onlayer top
            panda "拿 fetch, hold. Think about the situation. "
            jump bankQ1
            
        label grammarBank1:
            $ points -= 1 
            $ f.write('g')
            play sound "wrong.wav"
            hide bankteller normal
            show bankteller confused
            bankTeller "......"
            show pda backpack s onlayer top
            panda "吗 is redundant here. "
            jump bankQ1
            
        label conventionalBank1:
            $ points -= 1 
            $ f.write('c')
            play sound "wrong.wav"
            hide bankteller normal
            show bankteller confused
            bankTeller "......"
            show pda backpack s onlayer top
            panda "This is not the conventional way to withdraw money in the bank."
            jump bankQ1
            
        label rightBank1:
            $ points += 3 
            $ f.write('r ')
            $ f.write(str(points) + "\n")
            play sound "right.mp3"
            hide pda backpack s onlayer top
            show bankteller normal
            bankTeller "好的，您有银行卡吗？"
            player "有，在这里。"
            bankTeller "好的，这是您的现金，一共800块。"

        show bg insidebank
        show bankteller normal
        with dissolve
        "Now you have some cash for the trip. You're excited about the upcoming adventurous journey to take the panda home. You head to the train station." 

    # This starts the train scene. 
    # Add new music here.
    
        scene bg trainStation
        with dissolve
        show pda backpack
        "Today marks the start of your fantastic journey to Baobao's home." 
        "Baobao and you are both excited as you arrive at the train station."
        scene bg trainStation
        with dissolve
    
        "From the display board, you see that the train ticket to Chengdu/Sichuan is sold out for today." 
        "You have to get a ticket to go to Xi'an first. Xi'an is in between Beijing and Chengdu. You walk towards the ticket booth."

    # These display lines of dialogue.
   
    label trainIQ1:
        show ticketattendant normal
        hide pda backpack s onlayer top
        if first_trainQ1:
                $ f.write('trainQ1: ')
                $ first_trainQ1 = False
        ticketAttendant "你好。"
        
    menu trainQ1:
        "我买一张去西安的火车票，怎么样？":
            jump socioTrainQ1
        "我可以买一张去西安火车票呢？":
            jump grammarTrainQ1
        "我想买一张去西安的火车票。":
            jump rightTrainQ1
        "我能有火车票去西安吗？":
            jump conventionalTrainQ1
    
    label rightTrainQ1:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        jump trainIQ2
        
    label socioTrainQ1:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show ticketattendant angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "怎么样 is used to make a suggestion. Think about the situation. "
        jump trainIQ1
    
    label grammarTrainQ1:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show ticketattendant confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "呢 should be 吗. "
        jump trainIQ1
    
    label conventionalTrainQ1:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show ticketattendant confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to buy ticket. "
        jump trainIQ1
        
    label trainIQ2:
        hide pda backpack s onlayer top
        show ticketattendant normal
        ticketAttendant "下午两点半有一张，可以吗?"
        player "好。"

        scene bg insideTrain
        with dissolve
        "You get on the train with Baobao. Hours and hours have passed and you're not sure where to get off for Xi'an. So you ask the train attendant."

    label insidetrainQ1:
        scene bg insideTrain
        hide pda backpack s onlayer top
        if first_insidetrainQ1:
                $ f.write('insidetrainQ1: ')
                $ first_insidetrainQ1 = False
        show trainattendant normal
        with dissolve
       
    menu insidetrain01:
        "请问西安哪站下？":
            jump righttrain1
        "请问什么站下车去西安？":
            jump grammartrain1
        "我要去西安怎么走？":
            jump sociotrain1
        "请问怎么下车到西安？":
            jump conventionaltrain1
            
    label sociotrain1:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show trainattendant angry
        trainAttendant "......"
        show pda backpack s onlayer top
        with dissolve
        panda "怎么走 how to go somewhere. Think about the situation. "
        jump insidetrainQ1
        
    label grammartrain1:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show trainattendant confused
        trainAttendant "......"
        show pda backpack s onlayer top
        with dissolve
        panda "什么 should be 哪."
        jump insidetrainQ1
        
    label conventionaltrain1:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show trainattendant confused
        trainAttendant "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to ask for train stops. "
        jump insidetrainQ1
        
    label righttrain1:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        show trainattendant normal
        trainAttendant "下一站就是了。"
        player "谢谢啊。"
        
        show bg insideTrain
        hide trainattendant normal
        show pda backpack
        with dissolve
        "After a few hours, You have finally arrived! It's time for a rest in Xi'an before you head onto Sichuan..."
        
    #This starts the hotel scene. 
        scene bg hotel
        "You arrive at a hotel in Xi’an after a tiring train ride."
        "You check in to a hotel room."
        show hotelclerk normal
        with dissolve
        hotelclerk "你好，请跟我来。"
        player "好的。"
        show bg hotelroom
        with dissolve
        hide hotelclerk normal
        with dissolve
        "Finally, you can take a break in the hotel."
        "You have a good Chinese friend who is also in Xi'an. You text him to see if he wants to have dinner tomorrow."
        show text one
        with dissolve
        player "我来西安了。你明天有空一起吃晚饭吗？"
        hide text one
        show text two
        with dissolve
        friend "啊，太好了，好啊，明天六点在西安小吃见怎么样?"
        player "好，明天见！"
        "After contacting your friend, you just want to hang out in the hotel with Baobao tonight. Both of you need a good rest before your tour in Xi'an tomorrow."
   
        #store scene 
        scene bg clothes store
        with dissolve
        "Shanxi Restaurant is in a mall. You arrive at the mall half an hour early so you start to browse in a clothing store. The salesperson approaches you. But you’re just browsing."
    
    label storeQ1:
        if first_storeQ1:
                $ f.write('storeQ1: ')
                $ first_storeQ1 = False
        show sales normal 
        salesperson "您好。请问您要买什么?"
    
    menu store1:
        "我随便看看。":
            jump rightstore1
        "我不买什么。":
            jump sociostore1
        "我随便看着。":
            jump grammarstore1
        "我不知道。":
            jump conventionalstore1
   
    label sociostore1:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show sales angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "Think about the situation."
        jump storeQ1
    
    label grammarstore1:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“看着” indicates a state of looking."
        jump storeQ1

    label conventionalstore1:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to respond to shop assistant’s greeting."
        jump storeQ1
        
    label rightstore1:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve
        salesperson "好的，需要什么告诉我。"
        hide sales normal
        with dissolve
        "After walking around for a while, you found a T-shirt you want. You ask the price of the T-shirt and if you can try it on. "
    
    label storeQ2:
        hide pda backpack s onlayer top 
        if first_storeQ2:
                $ f.write('storeQ2: ')
                $ first_storeQ2 = False
        show sales normal
        with dissolve
    
    menu store2:
        "请问，这件T恤衫贵吗？":
            jump conventionalstore2
        "请问，这件T恤衫多少钱?":
            jump rightstore2
        "请问，这件T恤衫值多少钱？":
            jump sociostore2
        "请问，这件T恤衫多少块？":
            jump grammarstore2

    label sociostore2:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show sales angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“值” “worth” is too formal here. Think about the situation. "
        jump storeQ2
    
    label grammarstore2:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“多少块” should be “多少钱”."
        jump storeQ2

    label conventionalstore2:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to ask for the price."
        jump storeQ2
        
    label rightstore2:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve
        show sales normal
        salesperson "这件T恤衫120块。"
    
    label storeQ3:
        hide pda backpack s onlayer top
        if first_storeQ3:
                $ f.write('storeQ3: ')
                $ first_storeQ3 = False
        with dissolve
        show sales normal
        
    menu store3:
        "我想试一下吗?":
            jump grammarstore3
        "我可以穿一下吗？":
            jump conventionalstore3
        "我可以试一下吗？": 
            jump rightstore3
        "我可不可能试试？":
            jump sociostore3
            
    label sociostore3:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show sales angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“可不可能” is too elaborate here. Think about the situation."
        jump storeQ3
    
    label grammarstore3:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“吗” should be “好吗” here."
        jump storeQ3

    label conventionalstore3:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say it. "
        jump storeQ3
        
    label rightstore3:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve
        salesperson "当然可以。那里是试衣间。"
        "You try the clothes on in the fitting room and love it."
        show pda backpack
        with dissolve
        panda "It seems your taste in clothes isn’t too bad huh!"
        hide pda backpack
        with dissolve
    
    label storeQ4:
        hide pda backpack s onlayer top
        with dissolve
        if first_storeQ4:
                $ f.write('storeQ4: ')
                $ first_storeQ4 = False
        show sales normal
        "To purchase the clothes, you walk towards the salesperson."
    
    menu store4: 
        "请问在哪儿收款台？":
            jump grammarstore4
        "请问收款台在哪儿？":
            jump rightstore4
        "请问怎么给钱？":
            jump sociostore4
        "请问付钱给谁？":
            jump conventionalstore4
            
    label sociostore4:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show sales angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“怎么给钱” sounds a little rude here. Think about the situation. "
        jump storeQ4
    
    label grammarstore4:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "The sentence structure is not correct."
        jump storeQ4

    label conventionalstore4:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to ask where the cashier is."
        jump storeQ4
        
    label rightstore4:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve
        salesperson "往前走，在你的左手边就是了。"
        
    label storeQ5:
        hide pda backpack s onlayer top
        if first_storeQ5:
                $ f.write('storeQ5: ')
                $ first_storeQ5 = False
        with dissolve
        show sales normal 
        
    menu store5:
        "可以用信用卡吗？":
            jump rightstore5
        "用信用卡怎么样？":
            jump sociostore5
        "可以用信用卡呢？":
            jump grammarstore5
        "我用信用卡，可以不可以?":
            jump conventionalstore5
    
    label sociostore5:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show sales angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“怎么样” is used to make suggestion. Think about the situation. "
        jump storeQ5
    
    label grammarstore5:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“呢” is incorrect here. "
        jump storeQ5

    label conventionalstore5:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say it."
        jump storeQ5
        
    label rightstore5:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve
        salesperson "可以。"
        hide sales 
        show pda yawn
        with dissolve
        "After shopping, the panda seems really hungry, and you realize it’s almost time for dinner with your friend."
        
#restaurant scene
        scene bg restaurant
        hide pda backpack s onlayer top
        "The next day, after taking a tour in Xi'an with Baobao, you rush to the restaurant to meet your friend."
   
    label restaurantQ1:
        hide pda backpack s onlayer top
        show friend normal
        if first_restaurantQ1:
                $ f.write('restaurantQ1: ')
                $ first_restaurantQ1 = False
        with dissolve
        friend "来啦！"
        
    menu rest1:

        "非常抱歉，我太晚了。":
            jump sociorest1
        "不好意思，我很晚。":
            jump grammarrest1
        "不好意思，我来晚了。":
            jump rightrest1
        "对不起，我晚到":
            jump conventionalrest1
            
    label sociorest1:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show friend angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This expression might be too elaborate. Think about the situation."
        jump restaurantQ1
    
    label grammarrest1:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show friend confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "很晚 should be 晚了."
        jump restaurantQ1

    label conventionalrest1:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show friend confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to apologize for being late."
        jump restaurantQ1

    label rightrest1:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve
        show friend normal 
        friend "没关系，我刚到一会儿。"
        player "好久不见! 最近怎么样？"
        friend "不错，不错。你来西安真是太好了。饿了吧？我们点菜吧。"
        
    label restaurantQ2:
        scene bg restaurant
        hide pda backpack s onlayer top
        if first_restaurantQ2:
                $ f.write('restaurantQ2: ')
                $ first_restaurantQ2 = False
        show friend normal
        with dissolve
        
    menu rest2:
        
        "你点菜吧。":
            jump conventionalrest2
        "请问你想吃什么？":
            jump sociorest2
        "你想吃一下什么？":
            jump grammarrest2
        "你想吃点什么？":
            jump rightrest2
            
    label sociorest2:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show friend angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "请问 might be too formal here. Think about the situation. "
        jump restaurantQ2
    
    label grammarrest2:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show friend confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "一下 is used in the incorrect way."
        jump restaurantQ2

    label conventionalrest2:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show friend confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say it."
        jump restaurantQ2
        
    label rightrest2:
        $ points += 3
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve
        friend "我看看菜单。"
        player "鱼香肉丝怎么样？"
        friend "好啊，我还想吃饺子。"
        player "好，我来点菜。"
        
    label restaurantQ3:
        scene bg restaurant
        hide pda backpack s onlayer top
        show waiter normal
        with dissolve
        if first_restaurantQ3:
                $ f.write('restaurantQ3: ')
                $ first_restaurantQ3 = False
        waiter "请问点什么?"
    
    menu rest3:
        "给个鱼香肉丝和一盘饺子。":
            jump conventionalrest3
        "来鱼香肉丝和一个饺子。":
            jump grammarrest3
        "来个鱼香肉丝和一盘饺子。":
            jump rightrest3
        "请来个鱼香肉丝和一盘饺子吧。":
            jump sociorest3
    
    label sociorest3:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show waiter angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“请”“吧” sound too polite here. Think about the situation. "
        jump restaurantQ3
    
    label grammarrest3:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show waiter confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "Measure words are missing here."
        jump restaurantQ3

    label conventionalrest3:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show waiter confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to order food. "
        jump restaurantQ3
        
    label rightrest3:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        show waiter normal 
        waiter"好咧。"
        hide waiter normal
        scene bg food
        show restaurant food zoomin 
        with dissolve 
        "The food you ordered has arrived. They look delicious!" 
        "After a while, you and your friend finish your meal." 
        scene bg restaurant
        show restaurant food onlayer screens
        show friend normal
        friend "好,吃完了。"
        hide restaurant food onlayer screens
    
    label restaurantQ4:
        hide pda backpack s onlayer top
        hide friend normal
        if first_restaurantQ4:
                $ f.write('restaurantQ4: ')
                $ first_restaurantQ4 = False
        show waiter normal
        with dissolve
        waiter "请问需要什么?"
    
    menu rest4:
        "打包。":
            jump rightrest4
        "打包怎么样？":
            jump sociorest4
        "打包一下。":
            jump grammarrest4
        "打一个包。":
            jump conventionalrest4
    
    label sociorest4:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show waiter angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“怎么样” is used to make suggestion. Think about the situation. "
        jump restaurantQ4
    
    label grammarrest4:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show waiter confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“一下” is incorrect here."
        jump restaurantQ4

    label conventionalrest4:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show waiter confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say it. "
        jump restaurantQ4
        
    label rightrest4:
        $ points += 3
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve 
        waiter"好咧。"
        hide waiter normal 
        with dissolve
        "After saying goodbye to your friend, you leave the restaurant. It’s time to continue the journey onto Sichuan."

    scene bg trainStation
    with dissolve
    "Hours and hours passed on the train until you finally arrive at Chengdu."

#Here start street scene 
    scene bg street
    with dissolve
    "Finally, you brought the panda to his home Chengdu, Sichuan. After you get off the train, you see a busy street. It’s your first time in Chengdu, so you have no idea how to go to the Panda Base. So you decide to ask a stranger."
    
    label streetQ1:
        hide pda backpack s onlayer top
        with dissolve 
        if first_streetQ1:
                $ f.write('streetQ1: ')
                $ first_streetQ1 = False
        show stranger normal 
        with dissolve 
    
    menu street1:
        "请问，我想去熊猫基地，你知道吗?":
            jump conventionalstreet1
        "请问，你知道怎么去熊猫基地怎么走吗？":
            jump rightstreet1
        "请问，有没有可能请您告诉我怎么去熊猫基地呢?":
            jump sociostreet1
        "请问，去熊猫基地怎么办":
            jump grammarstreet1

    
    label sociostreet1:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show stranger angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“怎么去” “How to go somewhere”. Think about the situation."
        jump streetQ1
    
    label grammarstreet1:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“怎么办” “What to do”, is not used to ask for direction.  to ask for train stops."
        jump streetQ1

    label conventionalstreet1:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to ask for direction."
        jump streetQ1
        
    label rightstreet1:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve 
        show stranger normal 
        with dissolve
        stranger "一直往前走，到第二个路口右拐，就到了。"
        jump street2start
    
    label street2start:
        hide pda backpack s onlayer top
        if first_streetQ2:
                $ f.write('streetQ2: ')
                $ first_streetQ2 = False
        show stranger normal 
        stranger "一直往前走，到第二个路口右拐，就到了。"
        
    menu street2:
        "大概要多长?":
            jump grammarstreet2
        "时间要多少?":
            jump conventionalstreet2
        "你告诉我要多久?":
            jump sociostreet2
        "大概要多久?":
            jump rightstreet2

    label sociostreet2:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show stranger angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“告诉” “tell me” might be rude here. Think about the situation. "
        jump street2start
    
    label grammarstreet2:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“多长” “what is the length”."
        jump street2start

    label conventionalstreet2:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say it."
        jump street2start
        
    label rightstreet2:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve 
        show stranger normal 
        with dissolve
        stranger "大概20分钟吧。"
        jump street3start
    
    label street3start: 
        hide pda backpack s onlayer top
        if first_streetQ3:
                $ f.write('streetQ3: ')
                $ first_streetQ3 = False
        show stranger normal 
        stranger "大概20分钟吧。"
        
    menu street3:
        "谢谢你啊!":
            jump rightstreet3
        "非常感谢你的帮助!":
            jump sociostreet3
        "太谢谢!":
            jump grammarstreet3
        "谢谢你帮了我!":
            jump conventionalstreet3
        
    label sociostreet3:
        $ points -= 1 
        $ f.write('s')
        play sound "wrong.wav"
        show stranger angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This expression might be too elaborate and formal. Think about the situation."
        jump street3start
    
    label grammarstreet3:
        $ points -= 1 
        $ f.write('g')
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“太” should be used with “了” to modify adjectives."
        jump street3start

    label conventionalstreet3:
        $ points -= 1 
        $ f.write('c')
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say thank you to a stranger."
        jump street3start
        
    label rightstreet3:
        $ points += 3 
        $ f.write('r ')
        $ f.write(str(points) + "\n")
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve 
        stranger "不客气。"
    
    scene bg panda base 
    with dissolve
    "After about 30 minutes walk, you feel Baobao moving in your backpack. You put Baobao down and start to look around. Now on your right side, both you and Baobao are so excited to see a giant sign says “Chengdu Panda Base 成都大熊猫基地”."
    show pda yawn 
    with dissolve 
    panda "Thank you, kid! Couldn't have made it without you!"
    "Congratulations! You made it!"
    
 # This ends the game.
    return
