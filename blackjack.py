import tkinter
import random


def load_images(card_images) -> None:
    """
    Appends an ordered list of tuples, the first part being the value of the card and the
    second the tkinter-formatted image
    :param card_images: empty list (or any list to append to really)
    :return: None (though appends tuples to a given list)
    """
    suits = ['heart', 'spade', 'diamond', 'club']
    face_card = ['jack', 'queen', 'king']

    for suit in suits:
        for card in range(1, 11):
            name = f'cards/{str(card)}_{suit}.png'
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_card:
            name = f'cards/{str(card)}_{suit}.png'
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_cards(frame) -> int:
    """
    Takes the first card from randomly shuffled deck then places associated card image in given `frame.`
    :param frame: Frame card image is to be displayed in
    :return: value of card
    """
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand) -> int:
    """
    reads given `hand` and returns sum of score, considering aces.
    :param hand: list of cards in hand
    :return: total of card values
    """
    score = 0
    ace = False
    for next in hand:
        card_value = next[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_player():
    player_hand.append(deal_cards(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set('Dealer wins!')


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_cards(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)

    if player_score > 21:
        result_text.set('Dealer wins!')
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set('Player wins!')
    elif dealer_score > player_score:
        result_text.set('Dealer wins!')
    else:
        result_text.set('Draw!')


def new_game():
    """
    destroys card frames and resets card values and deck
    :return:
    """
    global player_card_frame
    global dealer_card_frame
    global cards
    global dealer_hand
    global player_hand
    global result_text

    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set('')

    dealer_hand = []
    player_hand = []
    deal_player()
    dealer_hand.append(deal_cards(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    main_window.mainloop()


def shuffle():
    random.shuffle(deck)

main_window = tkinter.Tk()


main_window.title('Blackjack')
main_window.geometry('640x480')
main_window.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_window, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)

dealer_card_frame = tkinter.Frame(card_frame, background='green')   # frame for dealer's cards
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)

tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, background='green')   # frame for player's cards
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, sticky='w', rowspan=3)

dealer_button = tkinter.Button(button_frame, text='Stick', command=deal_dealer)
dealer_button.grid(row=0, column=0, sticky='ew')

new_game_button = tkinter.Button(button_frame, text='New game', command=new_game)
new_game_button.grid(row=0, column=2, sticky='ew')

player_button = tkinter.Button(button_frame, text='Hit', command=deal_player)
player_button.grid(row=0, column=1, sticky='ew')

shuffle_button = tkinter.Button(button_frame, text='Shuffle', command=shuffle)
shuffle_button.grid(row=0, column=3, sticky='ew')

cards = []
load_images(cards)
print(cards)
# Create a new deck of cards and shuffle them using `random` module

deck = list(cards)
random.shuffle(deck)

# Lists to store dealer and player hands:
# dealer_hand = []
# player_hand = []

new_game()

main_window.mainloop()
