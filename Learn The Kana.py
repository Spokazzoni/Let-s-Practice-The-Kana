import random

def CharactersToPractice():
    romajiCharCount = 0
    hiraganaCharCount = 0
    katakanaCharCount = 0
    for i in romaji:
        for j in i:
            romajiCharCount += 1
    for i in hiragana:
        for j in i:
            hiraganaCharCount += 1
    for i in katakana:
        for j in i:
            katakanaCharCount += 1

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8' ,'9']
    print ("There are only ", romajiCharCount, " romanji characters, ", hiraganaCharCount + 2," hiragana and ", katakanaCharCount + 2, " katakana characters in the game")
    characterCount = input("How many romanji characters do you want to practice? ")

    i = 0
    while i < len(characterCount):
        if characterCount[i] not in numbers:
            print("You can only use numbers between 0 and ", romajiCharCount, " for the amount of characters you want to practice")
            print ("There are only ", romajiCharCount, " romanji characters, ", hiraganaCharCount," hiragana and ", katakanaCharCount, " katakana characters in the game")
            characterCount = input("How many romanji characters do you want to practice? ")
            i = -1

        elif i == len(characterCount) - 1 and int(characterCount) > romajiCharCount: 
            print ("You can only use numbers between 0 and ", romajiCharCount, " for the amount of characters you want to practice")   
            print ("There are only ", romajiCharCount, " romanji characters, ", hiraganaCharCount," hiragana and ", katakanaCharCount, " katakana characters in the game")
            characterCount = input("How many romanji characters do you want to practice? ")
            i = -1
        i += 1
        
    return int(characterCount)

def CharacterCheck (listIndex, characterIndex):

    if practiceType.upper() == "HIRAGANA":
        hiraganaCheck.append(hiragana[listIndex][characterIndex])
    elif practiceType.upper() == "KATAKANA":
        katakanaCheck.append(katakana[listIndex][characterIndex])
    else:
        hiraganaCheck.append(hiragana[listIndex][characterIndex])   
        katakanaCheck.append(katakana[listIndex][characterIndex])

def RandomCharacter():
    global elementAIndex
    global elementBIndex
    romajiElementA = romaji[random.randint(0, len(romaji) - 1)]
    while not romajiElementA:
            romajiElementA = romaji[random.randint(0, len(romaji) - 1)]

    romajiElementB = romajiElementA[random.randint(0, len(romajiElementA) - 1)]

    elementAIndex = romaji.index(romajiElementA)
    elementBIndex = romajiElementA.index(romajiElementB)

def Main():
    for i in range(CharactersToPractice()):
        RandomCharacter()

        while romaji[elementAIndex][elementBIndex] in kanaToWrite:
            RandomCharacter()

        kanaToWrite.append(romaji[elementAIndex][elementBIndex])

        CharacterCheck(elementAIndex, elementBIndex)
    # εμφανιση των χαρακτηρων που θα γραψω
    print (kanaToWrite)
    input("Press enter to compare your results")
    if practiceType.upper() == "HIRAGANA":
        print("Hiragana characters:\n" + str(hiraganaCheck))
    elif practiceType.upper() == "KATAKANA":
        print ("Katakana characters: \n" + str(katakanaCheck))
    else:
        print("Hiragana characters:\n" + str(hiraganaCheck))
        print ("Katakana characters: \n" + str(katakanaCheck))


hiragana = [
    ['あ','い', 'う', 'え', 'お'],
    ['か', 'き', 'く', 'け', 'こ'],
    ['が', 'ぎ', 'ぐ', 'げ', 'ご'],
    ['さ', 'し', 'す', 'せ', 'そ'],
    ['ざ', 'じ/ぢ', 'ず/づ', 'ぜ', 'ぞ'],
    ['た', 'ち', 'つ', 'て', 'と'],
    ['だ', 'で', 'ど'],
    ['な', 'に', 'ぬ', 'ね', 'の'],
    ['は', 'ひ', 'ふ', 'へ', 'ほ'],
    ['ば', 'び', 'ぶ', 'べ', 'ぼ'],
    ['ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ'],
    ['ま', 'み', 'む', 'め', 'も'],
    ['や', 'ゆ', 'よ'],
    ['ら', 'り', 'る', 'れ', 'ろ'],
    ['わ','を'],
    ['ん']]
katakana = [
    ['ア', 'イ', 'ウ', 'エ', 'オ'],
    ['カ', 'キ', 'ク', 'ケ', 'コ'],
    ['ガ', 'ギ', 'グ', 'ゲ', 'ゴ'],
    ['サ', 'シ', 'ス', 'セ', 'ソ'],
    ['ザ', 'ジ/ヂ', 'ズ/ヅ', 'ゼ', 'ゾ'],
    ['タ', 'チ', 'ツ', 'テ', 'ト'],
    ['ダ', 'デ', 'ド'],
    ['ナ', 'ニ', 'ヌ', 'ネ', 'ノ'],
    ['ハ', 'ヒ', 'フ', 'ヘ', 'ホ'],
    ['バ', 'ビ', 'ブ', 'ベ', 'ボ'],
    ['パ', 'ピ', 'プ', 'ペ', 'ポ'],
    ['マ', 'ミ', 'ム', 'メ', 'モ'],
    ['ヤ', 'ユ','ヨ'],
    ['ラ', 'リ', 'ル', 'レ','ロ'],
    ['ワ', 'ヲ'],
    ['ン']]
romaji = [
    ['a', 'i', 'u', 'e', 'o'],
    ['ka', 'ki', 'ku', 'ke', 'ko'],
    ['ga', 'gi', 'gu', 'ge', 'go'],
    ['sa', 'shi', 'su', 'se', 'so'],
    ['za', 'ji', 'zu', 'ze', 'zo'],
    ['ta', 'chi', 'tsu', 'te', 'to'],
    ['da', 'de', 'do'],
    ['na', 'ni', 'nu', 'ne', 'no'],
    ['ha', 'hi', 'fu', 'he', 'ho'],
    ['ba', 'bi', 'bu', 'be', 'bo'],
    ['pa', 'pi', 'pu', 'pe', 'po'],
    ['ma', 'mi', 'mu', 'me', 'mo'],
    ['ya', 'yu', 'yo'],
    ['ra', 'ri', 'ru', 're','ro'],
    ['wa', 'wo'],
    ['n']]
playAgainOptions = ["YES", "NO"]

play = True
while play:
    kanaToWrite = []
    hiraganaCheck = []
    katakanaCheck = []
    practiceModes = ['HIRAGANA', 'KATAKANA', 'BOTH']

    practiceType = input("Do you want to practice hiragana, katakana or both? ")

    while practiceType.upper() not in practiceModes:
        print ("The only practice modes are: Hiragana, Katakana and Both.")
        practiceType = input("Do you want to practice hiragana, katakana or both? ")

    Main()

    playAgain = input("Do you want to play again \n Yes/No: ")
    while playAgain.upper() not in playAgainOptions:
        print("Only acceptable answers are Yes or No")
        playAgain = input("Do you want to play again \n Yes/No: ")

    if playAgain.upper() == "NO":
        play = False