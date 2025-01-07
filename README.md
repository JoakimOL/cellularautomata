# Cellular Automata

### Keybindings:

- Mouseclick and drag: draw cells
- space: start/stop
- `s`: step one iteration
- numbers 1-5: change cell types (varies between automatas)

### Quick steps:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 src/main.py --help
pygame 2.6.1 (SDL 2.28.4, Python 3.10.12)
Hello from the pygame community. https://www.pygame.org/contribute.html
usage: AutomataApp [-h] [--verbose] [--debug] [--text] [--wrap] [--type {simple,rps,rps_spiral,gol}]

Cellular automatas are fun!

options:
  -h, --help            show this help message and exit
  --verbose             turn on more logging
  --debug               turn on a ton of logging
  --text                enable text
  --wrap                enable edge wrapping
  --type {simple,rps,rps_spiral,gol}
                        choose which rules to use. rps = rock-paper-scissors. gol = game of life
```
