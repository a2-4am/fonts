# https://sourceforge.net/projects/acme-crossass/
ACME=acme

# https://github.com/mach-kernel/cadius
CADIUS=cadius

# https://python.org/
PYTHON=python3

BUILDDISK=build/sample

asm: preconditions md
	$(ACME) -r build/sample.lst src/sample.a 2>build/log

font: preconditions
	$(PYTHON) font.py > src/ui.font.data.a

dist: preconditions asm
	cp ../common/blank.po "$(BUILDDISK)".po
	$(CADIUS) ADDFILE "${BUILDDISK}".po "/SAMPLE/" "build/SAMPLE.SYSTEM#FF2000"

clean:
	rm -rf build/

md:
	mkdir -p build

mount:
	open "$(BUILDDISK)".po

preconditions:
	@$(ACME) --version | grep -q "ACME, release" || (echo "ACME is not installed" && exit 1)
	@$(CADIUS) | grep -q "cadius v" || (echo "Cadius is not installed" && exit 1)
	@$(PYTHON) --version | grep -q "Python 3" || (echo "Python 3 is not installed" && exit 1)

all: clean font asm dist mount

al: all
