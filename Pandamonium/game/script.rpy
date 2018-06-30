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

image bg park="Park View Sketch.png"
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
screen Points_display:
     text "[points]" xpos 1180 ypos 0.090 size 35
     
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
        hide pda backpack s onlayer top 
        show prof happy
        professor "你好。请坐，有事吗？"
        player "李老师，不好意思，我家有点急事。"
        
    menu oq1:

        "我得有一个假期，好不好？":
            jump grammarOffice1
        "我可以请假几天呢？":
            jump usageOffice1
        "我想有几天不参加上课。":
            jump politeOffice1
        "我可以请几天假吗？":
            jump rightOffice1
            
    label grammarOffice1:
        $ points -= 1 
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top 
        with dissolve
        panda "得 might be too demanding here. Think about the context."
        jump officeQ1
        
    label usageOffice1:
        $ points -= 1 
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top 
        with dissolve
        panda "呢 is grammatically incorrect here."
        jump officeQ1
    
    label politeOffice1:
        $ points -= 1 
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top 
        with dissolve
        panda "不参加上课 is not the way Chinese people would say it."
        jump officeQ1
    
    label rightOffice1:
        $ points += 3 
        play sound "right.mp3"
        show prof happy
        professor "嗯，好吧。"
        jump officeQ2
        
    label officeQ2:
        show prof happy
        hide pda backpack s onlayer top 
        professor "不过你会错过明天的考试哦。"
    
    menu oq2:

        "我回来以后补考怎么样？":
            jump politeOffice2
        "我可不可以回来以后补考吗？":
            jump usageOffice2
        "我可不可以回来以后补考呢？":
            jump rightOffice2
        "我回来以后再考一次，好不好？":
            jump wrongOffice2
    
    label wrongOffice2:
        $ points -= 1 
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "再考一次 is not the conventional way to say it."
        jump officeQ2
        
    label usageOffice2:
        $ points -= 1 
        play sound "wrong.wav"
        show prof angry
        professor "......"
        show pda backpack s onlayer top
        with dissolve
        panda "吗 is redundant."
        jump officeQ2
    
    label politeOffice2:
        $ points -= 1 
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "怎么样 is used to make suggestions. Think about the situation here."
        jump officeQ2
    
    label rightOffice2:
        $ points += 3 
        play sound "right.mp3"
        show prof happy
        hide pda backpack s onlayer top
        professor "好的，那下星期回来以后补考吧。"
        jump moq3
    
    label officeQ3:
        hide pda backpack s onlayer top
        show prof happy
        professor "好的，那下星期回来以后补考吧。"
        
    menu moq3:
        "太好了！谢谢老师。":
            jump rightOffice3
        "太好了！谢了啊！":
            jump politeOffice3
        "太好了！很谢谢您了！":
            jump grammarOffice3
        "多谢！多谢啊！":
            jump wrongOffice3
        
    label politeOffice3:
        $ points -= 1 
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "谢了啊 is too informal. Think about the context."
        jump officeQ3
        
    label grammarOffice3:
        $ points -= 1 
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "We don't say 很......了."
        jump officeQ3
        
    label wrongOffice3:
        $ points -= 1 
        play sound "wrong.wav"
        show prof angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "That's not the way Chinese people would say it."
        jump officeQ3
    
    label rightOffice3:
        $ points += 3 
        play sound "right.mp3"
        show prof happy
        hide pda backpack s onlayer top
        professor "不客气。还有别的事吗？"
        player "没事了，谢谢老师。"
        jump moq4

    label officeQ4:
        hide pda backpack s onlayer top
        show prof happy
        player "没事了，谢谢老师。"
        
    menu moq4:

        "我要离开了！再见！":
            jump politeOffice4
        "那我先走了。再见！":
            jump rightOffice4
        "那我出去。再见！":
            jump grammarOffice4
        "我要走。再见！":
            jump wrongOffice4
            
    label politeOffice4:
        $ points -= 1 
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
        play sound "wrong.wav"
        show prof angry
        with dissolve
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "出去 means going out."
        jump officeQ4
    
    label wrongOffice4:
        $ points -= 1 
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
    vendor "买点苹果吗？"
    menu mfvq1:
        
        "苹果值多少钱？":
            jump politefruit1
        "苹果多少钱？":
            jump fvq2
        "苹果多少？":
            jump usagefruit1
        "一个苹果几块钱？":
            jump wrongfruit1
            
    label wrongfruit1:
        $ points -= 1 
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
    
    label usagefruit1:
        $ points -= 1 
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
    
    label politefruit1:
        $ points -= 1 
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
            
    label fvq2:
        $ points += 3 
        play sound "right.mp3"
        hide pda backpack s onlayer top
        hide vendor angry
        hide vendor confused
        show vendor normal
        vendor "六块钱一斤。"
        
    menu mfvq2:
        "便宜点吧！":
            jump fruitDone
        "便宜一下吧！":
            jump grammarfruit2
        "能不能打折？":
            jump usagefruit2
        "不要太贵了。":
            jump wrongfruit2
    
    label grammarfruit2:
        $ points -= 1 
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
    
    label usagefruit2:
        $ points -= 1 
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
    
    label wrongfruit2:
        $ points -= 1 
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

    label fruitDone:
        $ points += 3 
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
        show driv standard
        with dissolve
        
    menu mbdq1:
        "师傅，我要去中国银行，去不去？":
            jump politebd1
        "师傅，请问，向中国银行吗？":
            jump usagebd1
        "师傅，请问，到中国银行吗？":
            jump bdq2
        "师傅，请问，你的公共汽车去不去中国银行？":
            jump offtopicbd1
            
    label politebd1:
        $ points -= 1 
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "要 might be too demanding here. Think about the context/situation. "
        jump bdq1
    
    label usagebd1:
        $ points -= 1 
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "向 means towards. Is it correct here?"
        jump bdq1
        
    label offtopicbd1:
        $ points -= 1 
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "你的公共汽车 is not the conventional way to say it. "
        jump bdq1
            
    label bdq2:
        $ points += 3 
        play sound "right.mp3"
        hide pda backpack s onlayer top
        show driv happy
        with dissolve
        driver "这辆车不到。"
        
    menu mbdq2:
        
        "我怎么去中国银行？":
            jump politebd2
        "那请问哪辆车到中国银行吗？":
            jump usagebd2
        "那请问哪辆车到中国银行？":
            jump donebd
        "那请问什么公共汽车可以去中国银行？":
            jump contextbd2
            
    label politebd2:
        $ points -= 1 
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "怎么去 sounds a little demanding here. Think about the context/situation."
        jump bdq2
        
    label usagebd2:
        $ points -= 1 
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "吗 is redundant here."
        jump bdq2
        
    label contextbd2:
        $ points -= 1 
        play sound "wrong.wav"
        show driv confused
        with dissolve
        driver "......"
        show pda backpack s onlayer top
        with dissolve
        panda "什么公共汽车 is not the conventional way to refer to buses."
        jump bdq2
        
    label donebd:
        $ points += 3 
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
            show taxidriver normal
            with dissolve
            taxi "你好!"
    
        menu tq1:
            "请问我可不可以去中国银行？":
                jump grammarTaxi1
            "到中国银行。":
                jump usageTaxi1
            "去中国银行怎么样？":
                jump politeTaxi1
            "去中国银行。":
                jump rightTaxi1
                
        label grammarTaxi1:
            $ points -= 1 
            play sound "wrong.wav"
            show taxidriver confused
            taxi "......"
            show pda backpack s onlayer top
            with dissolve         
            panda "Is this too elaborate here? Think about the context/situation. "
            jump taxiQ1
            
        label usageTaxi1:
            $ points -= 1 
            play sound "wrong.wav"
            show taxidriver angry
            taxi "......"
            show pda backpack s onlayer top
            panda "到 means arrive. "
            jump taxiQ1
            
        label politeTaxi1:
            $ points -= 1 
            play sound "wrong.wav"
            show taxidriver confused
            taxi "......"
            show pda backpack s onlayer top
            panda "怎么样 is not the conventional way to give direction to the taxi driver."
            jump taxiQ1
            
        label rightTaxi1:
            $ points += 3 
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
            show bankteller normal
            bankTeller "您好，请问您需要办理什么业务?"

        menu bq2:
            "我想拿800块钱。":
                jump grammarBank1
            "我想取800块钱。":
                jump rightBank1
            "我想取800块钱吗? ":
                jump usageBank1
            "拿800块钱怎么样？":
                jump politeBank1
                
        label grammarBank1:
            $ points -= 1 
            play sound "wrong.wav"
            hide bankteller normal
            show bankteller angry
            bankTeller "......"
            show pda backpack s onlayer top
            panda "拿 fetch, hold. Think about the situation. "
            jump bankQ1
            
        label usageBank1:
            $ points -= 1 
            play sound "wrong.wav"
            hide bankteller normal
            show bankteller confused
            bankTeller "......"
            show pda backpack s onlayer top
            panda "吗 is redundant here. "
            jump bankQ1
            
        label politeBank1:
            $ points -= 1 
            play sound "wrong.wav"
            hide bankteller normal
            show bankteller confused
            bankTeller "......"
            show pda backpack s onlayer top
            panda "This is not the conventional way to withdraw money in the bank."
            jump bankQ1
            
        label rightBank1:
            $ points += 3 
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
        ticketAttendant "你好。"
        
    menu trainQ1:
        "我买一张去西安的火车票，怎么样？":
            jump socioTrainQ1
        "我可以买一张去西安火车票呢？":
            jump pragTrainQ1
        "我想买一张去西安的火车票。":
            jump correctTrainQ1
        "我能有火车票去西安吗？":
            jump nonConTrainQ1
    
    label correctTrainQ1:
        $ points += 3 
        play sound "right.mp3"
        hide pda backpack s onlayer top
        jump trainIQ2
        
    label socioTrainQ1:
        $ points -= 1 
        play sound "wrong.wav"
        show ticketattendant angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "怎么样 is used to make a suggestion. Think about the situation. "
        jump trainIQ1
    
    label pragTrainQ1:
        $ points -= 1 
        play sound "wrong.wav"
        show ticketattendant confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "呢 should be 吗. "
        jump trainIQ1
    
    label nonConTrainQ1:
        $ points -= 1 
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
        show trainattendant normal
        with dissolve
       
    menu insidetrain01:
        "请问西安哪站下？":
            jump correcttrain1
        "请问什么站下车去西安？":
            jump grammartrain1
        "我要去西安怎么走？":
            jump sociotrain1
        "请问怎么下车到西安？":
            jump conventionaltrain1
            
    label sociotrain1:
        $ points -= 1 
        play sound "wrong.wav"
        show trainattendant angry
        trainAttendant "......"
        show pda backpack s onlayer top
        with dissolve
        panda "怎么走 how to go somewhere. Think about the situation. "
        jump insidetrainQ1
        
    label grammartrain1:
        $ points -= 1 
        play sound "wrong.wav"
        show trainattendant confused
        trainAttendant "......"
        show pda backpack s onlayer top
        with dissolve
        panda "什么 should be 哪."
        jump insidetrainQ1
        
    label conventionaltrain1:
        $ points -= 1 
        play sound "wrong.wav"
        show trainattendant confused
        trainAttendant "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to ask for train stops. "
        jump insidetrainQ1
        
    label correcttrain1:
        $ points += 3 
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
        show sales normal 
        salesperson "您好。请问您要买什么?"
    
    menu store1:
        "我随便看看。":
            jump correctstore1
        "我不买什么。":
            jump sociostore1
        "我随便看着。":
            jump grammarstore1
        "我不知道。":
            jump conventionalstore1
   
    label sociostore1:
        $ points -= 1 
        play sound "wrong.wav"
        show sales angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "Think about the situation."
        jump storeQ1
    
    label grammarstore1:
        $ points -= 1 
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“看着” indicates a state of looking."
        jump storeQ1

    label conventionalstore1:
        $ points -= 1 
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to respond to shop assistant’s greeting."
        jump storeQ1
        
    label correctstore1:
        $ points += 3 
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve
        salesperson "好的，需要什么告诉我。"
        hide sales normal
        with dissolve
        "After walking around for a while, you found a T-shirt you want. You ask the price of the T-shirt and if you can try it on. "
    
    label storeQ2:
        show sales normal
        with dissolve
    
    menu store2:
        "请问，这件T恤衫贵吗？":
            jump conventionalstore2
        "请问，这件T恤衫多少钱?":
            jump correctstore2
        "请问，这件T恤衫值多少钱？":
            jump sociostore2
        "请问，这件T恤衫多少块？":
            jump grammarstore2

    label sociostore2:
        $ points -= 1 
        play sound "wrong.wav"
        show sales angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“值” “worth” is too formal here. Think about the situation. "
        jump storeQ2
    
    label grammarstore2:
        $ points -= 1 
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“多少块” should be “多少钱”."
        jump storeQ2

    label conventionalstore2:
        $ points -= 1 
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to ask for the price."
        jump storeQ2
        
    label correctstore2:
        $ points += 3 
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve
        show sales normal
        salesperson "这件T恤衫120块。"
    
    menu store3:
        "我想试一下吗?":
            jump grammarstore3
        "我可以穿一下吗？":
            jump conventionalstore3
        "我可以试一下吗？": 
            jump correctstore3
        "我可不可能试试？":
            jump sociostore3
            
    label sociostore3:
        $ points -= 1 
        play sound "wrong.wav"
        show sales angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“可不可能” is too elaborate here. Think about the situation."
        jump correctstore2
    
    label grammarstore3:
        $ points -= 1 
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“吗” should be “好吗” here."
        jump correctstore2

    label conventionalstore3:
        $ points -= 1 
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say it. "
        jump correctstore2
        
    label correctstore3:
        $ points += 3 
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
        show sales normal
        "To purchase the clothes, you walk towards the salesperson."
    
    menu store4: 
        "请问在哪儿收款台？":
            jump grammarstore4
        "请问收款台在哪儿？":
            jump correctstore4
        "请问怎么给钱？":
            jump sociostore4
        "请问付钱给谁？":
            jump conventionalstore4
            
    label sociostore4:
        $ points -= 1 
        play sound "wrong.wav"
        show sales angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“怎么给钱” sounds a little rude here. Think about the situation. "
        jump storeQ4
    
    label grammarstore4:
        $ points -= 1 
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "The sentence structure is not correct."
        jump storeQ4

    label conventionalstore4:
        $ points -= 1 
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to ask where the cashier is."
        jump storeQ4
        
    label correctstore4:
        $ points += 3 
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve
        salesperson "往前走，在你的左手边就是了。"
        
    label storeQ5:
        hide pda backpack s onlayer top
        with dissolve
        show sales normal 
        
    menu store5:
        "可以用信用卡吗？":
            jump correctstore5
        "用信用卡怎么样？":
            jump sociostore5
        "可以用信用卡呢？":
            jump grammarstore5
        "我用信用卡，可以不可以?":
            jump conventionalstore5
    
    label sociostore5:
        $ points -= 1 
        play sound "wrong.wav"
        show sales angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“怎么样” is used to make suggestion. Think about the situation. "
        jump storeQ5
    
    label grammarstore5:
        $ points -= 1 
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“呢” is incorrect here. "
        jump storeQ5

    label conventionalstore5:
        $ points -= 1 
        play sound "wrong.wav"
        show sales confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say it."
        jump storeQ5
        
    label correctstore5:
        $ points += 3 
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
        with dissolve
        friend "来啦！"
        
    menu rest1:

        "非常抱歉，我太晚了。":
            jump sociorest1
        "不好意思，我很晚。":
            jump grammarrest1
        "不好意思，我来晚了。":
            jump correctrest1
        "对不起，我晚到":
            jump conventionalrest1
            
    label sociorest1:
        $ points -= 1 
        play sound "wrong.wav"
        show friend angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This expression might be too elaborate. Think about the situation."
        jump restaurantQ1
    
    label grammarrest1:
        $ points -= 1 
        play sound "wrong.wav"
        show friend confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "很晚 should be 晚了."
        jump restaurantQ1

    label conventionalrest1:
        $ points -= 1 
        play sound "wrong.wav"
        show friend confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to apologize for being late."
        jump restaurantQ1

    label correctrest1:
        $ points += 3 
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
        show friend normal
        
    menu rest2:
        
        "你点菜吧。":
            jump conventionalrest2
        "请问你想吃什么？":
            jump sociorest2
        "你想吃一下什么？":
            jump grammarrest2
        "你想吃点什么？":
            jump correctrest2
            
    label sociorest2:
        $ points -= 1 
        play sound "wrong.wav"
        show friend angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "请问 might be too formal here. Think about the situation. "
        jump restaurantQ2
    
    label grammarrest2:
        $ points -= 1 
        play sound "wrong.wav"
        show friend confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "一下 is used in the incorrect way."
        jump restaurantQ2

    label conventionalrest2:
        $ points -= 1 
        play sound "wrong.wav"
        show friend confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say it."
        jump restaurantQ2
        
    label correctrest2:
        $ points += 3 
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
        waiter "请问点什么?"
    
    menu rest3:
        "给个鱼香肉丝和一盘饺子。":
            jump conventionalrest3
        "来鱼香肉丝和一个饺子。":
            jump grammarrest3
        "来个鱼香肉丝和一盘饺子。":
            jump correctrest3
        "请来个鱼香肉丝和一盘饺子吧。":
            jump sociorest3
    
    label sociorest3:
        $ points -= 1 
        play sound "wrong.wav"
        show waiter angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“请”“吧” sound too polite here. Think about the situation. "
        jump restaurantQ3
    
    label grammarrest3:
        $ points -= 1 
        play sound "wrong.wav"
        show waiter confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "Measure words are missing here."
        jump restaurantQ3

    label conventionalrest3:
        $ points -= 1 
        play sound "wrong.wav"
        show waiter confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to order food. "
        jump restaurantQ3
        
    label correctrest3:
        $ points += 3 
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
        show waiter normal
        with dissolve
        waiter "请问需要什么?"
    
    menu rest4:
        "打包。":
            jump correctrest4
        "打包怎么样？":
            jump sociorest4
        "打包一下。":
            jump grammarrest4
        "打一个包。":
            jump conventionalrest4
    
    label sociorest4:
        $ points -= 1 
        play sound "wrong.wav"
        show waiter angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“怎么样” is used to make suggestion. Think about the situation. "
        jump restaurantQ4
    
    label grammarrest4:
        $ points -= 1 
        play sound "wrong.wav"
        show waiter confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“一下” is incorrect here."
        jump restaurantQ4

    label conventionalrest4:
        $ points -= 1 
        play sound "wrong.wav"
        show waiter confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say it. "
        jump restaurantQ4
        
    label correctrest4:
        $ points += 3 
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
        show stranger normal 
        with dissolve 
    
    menu street1:
        "请问，我想去熊猫基地，你知道吗?":
            jump conventionalstreet1
        "请问，你知道怎么去熊猫基地怎么走吗？":
            jump correctstreet1
        "请问，有没有可能请您告诉我怎么去熊猫基地呢?":
            jump sociostreet1
        "请问，去熊猫基地怎么办":
            jump grammarstreet1

    
    label sociostreet1:
        $ points -= 1 
        play sound "wrong.wav"
        show stranger angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“怎么去” “How to go somewhere”. Think about the situation."
        jump streetQ1
    
    label grammarstreet1:
        $ points -= 1 
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“怎么办” “What to do”, is not used to ask for direction.  to ask for train stops."
        jump streetQ1

    label conventionalstreet1:
        $ points -= 1 
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to ask for direction."
        jump streetQ1
        
    label correctstreet1:
        $ points += 3 
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve 
        show stranger normal 
        with dissolve
        stranger "一直往前走，到第二个路口右拐，就到了。"
        jump street2
    
    label street2start:
        hide pda backpack s onlayer top
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
            jump correctstreet2

    label sociostreet2:
        $ points -= 1 
        play sound "wrong.wav"
        show stranger angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“告诉” “tell me” might be rude here. Think about the situation. "
        jump street2start
    
    label grammarstreet2:
        $ points -= 1 
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“多长” “what is the length”."
        jump street2start

    label conventionalstreet2:
        $ points -= 1 
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say it."
        jump street2start
        
    label correctstreet2:
        $ points += 3 
        play sound "right.mp3"
        hide pda backpack s onlayer top
        with dissolve 
        show stranger normal 
        with dissolve
        stranger "大概20分钟吧。"
        jump street3
    
    label street3start: 
        hide pda backpack s onlayer top
        show stranger normal 
        stranger "大概20分钟吧。"
        
    menu street3:
        "谢谢你啊!":
            jump correctstreet3
        "非常感谢你的帮助!":
            jump sociostreet3
        "太谢谢!":
            jump grammarstreet3
        "谢谢你帮了我!":
            jump conventionalstreet3
        
    label sociostreet3:
        $ points -= 1 
        play sound "wrong.wav"
        show stranger angry
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This expression might be too elaborate and formal. Think about the situation."
        jump street3start
    
    label grammarstreet3:
        $ points -= 1 
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "“太” should be used with “了” to modify adjectives."
        jump street3start

    label conventionalstreet3:
        $ points -= 1 
        play sound "wrong.wav"
        show stranger confused
        "......"
        show pda backpack s onlayer top
        with dissolve
        panda "This is not the conventional way to say thank you to a stranger."
        jump street3start
        
    label correctstreet3:
        $ points += 3 
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
