import os


def render(board_state, height, width, cursor_pos):
    printing_buffer = ''
    horizontal_spacer = ''

    clear_terminal()

    # Create a proper width horizontal spacer
    for i in range(width):
        horizontal_spacer += '- - '

    for index, row in enumerate(board_state):
        for count, cell in enumerate(board_state[index], start=1):
            # Mark the cursor
            if cursor_pos[1] == index and cursor_pos[0] == count - 1:
                printing_buffer += '█' + chr_id(cell) + '█'
            else:
                printing_buffer += ' ' + chr_id(cell) + ' '

            # Add a vertical spacer if not at the edge
            if count + 1 <= len(board_state[index]):
                printing_buffer += '|'

        print(printing_buffer)

        # Add a horizontal spacer if not at the edge
        if index + 1 < len(board_state):
            print(horizontal_spacer)

        # Clear printing_buffer
        printing_buffer = ''


# Returns a character mapped to a given number
def chr_id(i):
    character_map = {
        0: ' ',
        1: 'x',
        2: 'o'
    }
    try:
        return character_map.get(i)
    except:
        print("No character mapped for ID: " + i)


# Clear the terminal/console
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
