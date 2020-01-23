import pygame
from time import sleep


def get_name(win, max_len, pos):
    pygame.init()

    font = pygame.font.Font(None, 32)

    input_box = pygame.Rect(*pos, max_len * 10, 30)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = True
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key == pygame.QUIT:
                        return False
                    else:
                        text += event.unicode

        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(win, color, input_box, 2)

        pygame.display.flip()
        sleep(0.1)

    return text[:max_len:]


if __name__ == '__main__':
    pygame.init()
    display_size = pygame.display.Info()
    x, y = display_size.current_w, display_size.current_h
    win = pygame.display.set_mode((x, y))
    print(get_name(win, 10, (x / 2 - 50, y // 2)))