antlr4 = java -Xmx500M -cp "/usr/local/lib/antlr-4.9.2-complete.jar" org.antlr.v4.Tool
nice_grammar = nice.g4

grammar: src/$(nice_grammar)
	cd src;	$(antlr4) -Dlanguage=Python3 -visitor $(nice_grammar); cd ..

build: grammar

run: build src/nice.py
	python3 nice.py