all: check_types check_style fix_style unittest localtest submit clean

unittest:
	pytest unittests.py
	@echo "\n All unittest cases worked...\n"

localtest:
	cat 1.in | python3 cosmicpathoptimization.py | diff - 1.ans
	@echo "\n All kattis sample test data test done...\n"

check_style:
	flake8 cosmicpathoptimization.py --count --show-source --statistics
	flake8 unittests.py --count --show-source --statistics
	@echo "\n flake8 Pass!\n"
fix_style:
	autopep8 --in-place --recursive --aggressive --aggressive .
	@echo "\n autopep8 fixed style\n "
check_types:
	mypy --disallow-untyped-defs --strict cosmicpathoptimization.py
	mypy --disallow-untyped-defs --strict unittests.py
	@echo "\n mypy Pass!\n"

submit:
	echo "y" | kattis cosmicpathoptimization.py
	@echo "\n kattis-cli Pass!\n"

clean:
	rm -rf __pycache__
	rm -rf *.pyc