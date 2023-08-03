import streamlit as st
import random

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [{'suit': suit, 'value': value} for suit in suits for value in values]

def deal_cards(players):
    # Make a copy of the original deck to avoid modifying the original deck
    current_deck = list(deck)
    hands = [[] for _ in range(players)]
    random.shuffle(current_deck)
    
    for _ in range(2):
        for i in range(players):
            card = current_deck.pop()
            hands[i].append(card)
            
    return hands

# Function to evaluate the hand strength
def evaluate_hand(hand):
    # Implement your poker hand evaluation logic here
    # For simplicity, let's just assume the hand with the highest value wins
    hand_values = [values.index(card['value']) for card in hand]
    return max(hand_values)

# Main poker simulation function
def poker_simulation(players, rounds):
    results = []
    for round_num in range(1, rounds + 1):
        round_result = {"Round": round_num, "Players": [], "Winning Hand": None}

        # Deal cards to players
        hands = deal_cards(players)

        # Evaluate hand strength for each player
        hand_strengths = [evaluate_hand(hand) for hand in hands]

        # Find the winning hand
        max_strength = max(hand_strengths)
        winners = [i for i, strength in enumerate(hand_strengths) if strength == max_strength]

        # Add player hands to the result
        for i, hand in enumerate(hands):
            round_result["Players"].append({"Player": i+1, "Hand": hand, "Hand Strength": hand_strengths[i]})

        # Add winning hand to the result
        round_result["Winning Hand"] = {"Strength": max_strength, "Winning Players": winners}

        # Add round result to the overall results
        results.append(round_result)

    return results

# Streamlit app
def main():
    st.title("Poker Simulation App")

    players = st.slider("Select number of players:", 2, 10, 8)
    rounds = st.slider("Select number of rounds:", 1, 10, 5)

    if st.button("Simulate Poker"):
        results = poker_simulation(players, rounds)
        
        # Display the results
        for round_result in results:
            st.subheader(f"Round {round_result['Round']}")
            for player in round_result['Players']:
                st.write(f"Player {player['Player']} hand: {player['Hand']}, Hand Strength: {player['Hand Strength']}")
            st.write(f"Winning Hand Strength: {round_result['Winning Hand']['Strength']} (Winning Players: {', '.join(str(w+1) for w in round_result['Winning Hand']['Winning Players'])})")

if __name__ == "__main__":
    main()
