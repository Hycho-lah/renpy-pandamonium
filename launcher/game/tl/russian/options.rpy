﻿
translate russian strings:

    # options.rpy:1
    old "## This file contains options that can be changed to customize your game."
    new "## Данный файл содержит опции, способные изменить вашу игру."

    # options.rpy:4
    old "## Lines beginning with two '#' marks are comments, and you shouldn't uncomment them. Lines beginning with a single '#' mark are commented-out code, and you may want to uncomment them when appropriate."
    new "## Строки, начинающиеся  с двух '#' — комментарии, и вы не должны их раскомментировать. Строки, начинающиеся с одной '#' — комментированный код, который вы можете раскомментировать, если вы считаете это нужным."

    # options.rpy:10
    old "## Basics"
    new "## Основное"

    # options.rpy:12
    old "## A human-readable name of the game. This is used to set the default window title, and shows up in the interface and error reports."
    new "## Читаемое название игры. Используется при установке стандартного заголовка окна, показывается в интерфейсе и отчётах об ошибках."

    # options.rpy:15
    old "## The _() surrounding the string marks it as eligible for translation."
    new "## Символы \"_()\", окружающие название, отмечают его как пригодное для перевода."

    # options.rpy:17
    old "Ren'Py 7 Default GUI"
    new "Ren'Py 7 Стандартный GUI"

    # options.rpy:20
    old "## Determines if the title given above is shown on the main menu screen. Set this to False to hide the title."
    new "## Определяет, показывать ли заголовок, данный выше, на экране главного меню. Установите на False, чтобы спрятать заголовок."

    # options.rpy:26
    old "## The version of the game."
    new "## Версия игры."

    # options.rpy:31
    old "## Text that is placed on the game's about screen. To insert a blank line between paragraphs, write \\n\\n."
    new "## Текст, помещённый в экран \"Об игре\". Чтобы вставить пустую линию между параграфами, напишите \\n\\n."

    # options.rpy:37
    old "## A short name for the game used for executables and directories in the built distribution. This must be ASCII-only, and must not contain spaces, colons, or semicolons."
    new "## Короткое название игры, используемое для исполняемых файлов и директорий при постройке дистрибутивов. Оно должно содержать текст формата ASCII и не должно содержать пробелы, двоеточия и точки с запятой."

    # options.rpy:44
    old "## Sounds and music"
    new "## Звуки и музыка"

    # options.rpy:46
    old "## These three variables control which mixers are shown to the player by default. Setting one of these to False will hide the appropriate mixer."
    new "## Эти три переменные контролируют соответствующие микшеры громкости в настройках, которые пользователь может настраивать по умолчанию. Изменив один из параметров на False, скроется соответствующий микшер."

    # options.rpy:55
    old "## To allow the user to play a test sound on the sound or voice channel, uncomment a line below and use it to set a sample sound to play."
    new "## Чтобы разрешить пользователю тестировать громкость на звуковом или голосовом каналах, раскомментируйте строчку и настройте пример звука для прослушивания."

    # options.rpy:62
    old "## Uncomment the following line to set an audio file that will be played while the player is at the main menu. This file will continue playing into the game, until it is stopped or another file is played."
    new "## Раскомментируйте следующую строчку, чтобы настроить аудиофайл, который будет проигрываться в главном меню. Этот файл продолжит проигрываться во время игры, если не будет остановлен, или не начнёт проигрываться другой аудиофайл."

    # options.rpy:69
    old "## Transitions"
    new "## Переходы"

    # options.rpy:71
    old "## These variables set transitions that are used when certain events occur. Each variable should be set to a transition, or None to indicate that no transition should be used."
    new "## Эти переменные задают переходы, используемые в различных событиях. Каждая переменная должна задавать переход или None, чтобы указать то, что переход не должен использоваться."

    # options.rpy:75
    old "## Entering or exiting the game menu."
    new "## Вход и выход в игровое меню."

    # options.rpy:81
    old "## A transition that is used after a game has been loaded."
    new "## Переход, используемый после того, как игра загрузилась."

    # options.rpy:86
    old "## Used when entering the main menu after the game has ended."
    new "## Используется при входе в главное меню после того, как игра закончится."

    # options.rpy:91
    old "## A variable to set the transition used when the game starts does not exist. Instead, use a with statement after showing the initial scene."
    new "## Переменная, устанавливающая переход, используемый, когда старт игры не существует. Вместо неё используйте функцию with после показа начальной сценки."

    # options.rpy:96
    old "## Window management"
    new "## Управление окнами"

    # options.rpy:98
    old "## This controls when the dialogue window is displayed. If \"show\", it is always displayed. If \"hide\", it is only displayed when dialogue is present. If \"auto\", the window is hidden before scene statements and shown again once dialogue is displayed."
    new "## Эта строка контролирует, когда появляется диалоговое окно. Если \"show\", оно всегда показано. Если \"hide\", оно показывается, только когда представлен диалог. Если \"auto\", окно скрыто до оператора scene и показывается, когда появляется диалог."

    # options.rpy:103
    old "## After the game has started, this can be changed with the \"window show\", \"window hide\", and \"window auto\" statements."
    new "## После того как игра началась, это может быть изменено с помощью \"window show\", \"window hide\", и \"window auto\"."

    # options.rpy:109
    old "## Transitions used to show and hide the dialogue window"
    new "## Переходы, используемые при показе и скрытии диалогового окна"

    # options.rpy:115
    old "## Preference defaults"
    new "## Стандартные настройки"

    # options.rpy:117
    old "## Controls the default text speed. The default, 0, is infinite, while any other number is the number of characters per second to type out."
    new "## Контролирует стандартную скорость текста. По умолчанию это 0 — мгновенно, в то время как любая другая цифра, это количество символов, печатаемых в секунду."

    # options.rpy:123
    old "## The default auto-forward delay. Larger numbers lead to longer waits, with 0 to 30 being the valid range."
    new "## Стандартная задержка авто-чтения. Большие значения означают долгие ожидания, а от 0 до 30 — вполне допустимый диапазон."

    # options.rpy:129
    old "## Save directory"
    new "## Директория сохранений"

    # options.rpy:131
    old "## Controls the platform-specific place Ren'Py will place the save files for this game. The save files will be placed in:"
    new "## Контролирует зависимое от платформы место, куда Ren'Py будет складывать файлы сохранения этой игры. Файлы сохранений будут храниться в:"

    # options.rpy:134
    old "## Windows: %APPDATA\\RenPy\\<config.save_directory>"
    new "## Windows: %APPDATA\\RenPy\\<config.save_directory>"

    # options.rpy:136
    old "## Macintosh: $HOME/Library/RenPy/<config.save_directory>"
    new "## Macintosh: $HOME/Library/RenPy/<config.save_directory>"

    # options.rpy:138
    old "## Linux: $HOME/.renpy/<config.save_directory>"
    new "## Linux: $HOME/.renpy/<config.save_directory>"

    # options.rpy:140
    old "## This generally should not be changed, and if it is, should always be a literal string, not an expression."
    new "## Оно обычно не должно изменяться, а если и изменилось, должно быть текстовой строчкой, а не выражением."

    # options.rpy:146
    old "## Icon"
    new "## Иконка"

    # options.rpy:148
    old "## The icon displayed on the taskbar or dock."
    new "## Иконка, показываемая на панели задач или на dock."

    # options.rpy:153
    old "## Build configuration"
    new "## Настройка Дистрибутива"

    # options.rpy:155
    old "## This section controls how Ren'Py turns your project into distribution files."
    new "## Эта секция контролирует, как Ren'Py строит дистрибутивные файлы из вашего проекта."

    # options.rpy:160
    old "## The following functions take file patterns. File patterns are case- insensitive, and matched against the path relative to the base directory, with and without a leading /. If multiple patterns match, the first is used."
    new "## Следующие функции избирают образцы файлов. Образцы файлов не учитывают регистр и соответствующе зависят от директории base, с или без учёта /, задающей директорию. Если обнаруживается множество одноимённых файлы, используется только первый."

    # options.rpy:165
    old "## In a pattern:"
    new "## Инструкция:"

    # options.rpy:167
    old "## / is the directory separator."
    new "## / — разделитель директорий."

    # options.rpy:169
    old "## * matches all characters, except the directory separator."
    new "## * включает в себя все символы, исключая разделитель директорий."

    # options.rpy:171
    old "## ** matches all characters, including the directory separator."
    new "## ** включает в себя все символы, включая разделитель директорий."

    # options.rpy:173
    old "## For example, \"*.txt\" matches txt files in the base directory, \"game/**.ogg\" matches ogg files in the game directory or any of its subdirectories, and \"**.psd\" matches psd files anywhere in the project."
    new "## Например, \"*.txt\" берёт все файлы в формате txt из директории base, \"game/**.ogg\" берёт все файлы ogg из директории game и всех поддиректорий, а \"**.psd\" берёт все файлы psd из любого места проекта."

    # options.rpy:177
    old "## Classify files as None to exclude them from the built distributions."
    new "## Классифицируйте файлы как None, чтобы исключить их из дистрибутивов."

    # options.rpy:185
    old "## To archive files, classify them as 'archive'."
    new "## Чтобы архивировать файлы, классифицируйте их, например, как 'archive'."

    # options.rpy:190
    old "## Files matching documentation patterns are duplicated in a mac app build, so they appear in both the app and the zip file."
    new "## Файлы, соответствующие образцам документации, дублируются в приложениях Mac так, чтобы они появлялись и в приложении, и в zip архиве."

    # options.rpy:196
    old "## A Google Play license key is required to download expansion files and perform in-app purchases. It can be found on the \"Services & APIs\" page of the Google Play developer console."
    new "## Лицензионный ключ Google Play требуется для загрузки файлов расширений и поддержки внутриигровых покупок. Он может быть найден на странице \"Services & APIs\" консоли разработчика Google Play."

    # options.rpy:203
    old "## The username and project name associated with an itch.io project, separated by a slash."
    new "## Имя пользователя и название проекта, ассоциированные с проектом на itch.io, разделённые дробью."

