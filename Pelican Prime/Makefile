# https://sourceforge.net/projects/acme-crossass/
ACME=acme

# https://github.com/mach-kernel/cadius
CADIUS=cadius

# https://python.org/
PYTHON=python3

BUILDDIR=build
SOURCES=$(wildcard src/*.a)
FONTDATA=src/ui.font.data.a
EXE=$(BUILDDIR)/SAMPLE.SYSTEM\#FF2000
DISKVOLUME=SAMPLE
BUILDDISK=$(BUILDDIR)/sample.po

.PHONY: clean mount all

$(BUILDDISK): $(EXE)
	cp ../common/blank.po "$@"
	$(CADIUS) ADDFILE "$@" "/$(DISKVOLUME)/" "$(EXE)"

$(EXE): $(SOURCES) $(FONTDATA) | $(BUILDDIR)
	$(ACME) -r build/sample.lst src/sample.a

$(FONTDATA): font.py font-master.txt
	$(PYTHON) font.py > "$@"

mount: $(BUILDDISK)
	open "$(BUILDDISK)"

clean:
	rm -rf "$(BUILDDIR)"

$(BUILDDIR):
	@mkdir -p "$@"

all: clean mount

.NOTPARALLEL:
