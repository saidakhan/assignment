test:
	@$(MAKE) -sk test-all

test-all:	test-priority-queue test-cups test-spell-check

test-priority-queue: priority_queue.py
	@echo Testing PriorityQueue ...
	@curl -sLO https://raw.githubusercontent.com/nd-cse-20312-fa23/cse-20312-fa23-assignments/master/homework08/priority_queue_test.py
	@chmod +x ./priority_queue_test.py
	@./priority_queue_test.py -v
	@echo

test-cups: cups.py
	@echo Testing Cups...
	@curl -sLO https://raw.githubusercontent.com/nd-cse-20312-fa23/cse-20312-fa23-assignments/master/homework08/cups_test.py
	@chmod +x ./cups_test.py
	@./cups_test.py -v
	@echo

test-spell-check: spell_check.py
	@echo Testing SpellCheck ...
	@curl -sLO https://raw.githubusercontent.com/nd-cse-20312-fa23/cse-20312-fa23-assignments/master/homework08/spell_check_test.py
	@chmod +x ./spell_check_test.py
	@./spell_check_test.py -v
	@echo

clean:
	@rm -f priority_queue_test.py cups_test.py spell_check_test.py
