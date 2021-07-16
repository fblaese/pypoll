#!/usr/bin/env python3

import select
import os

# fixme: proper error handling
fd1 = open("./pipe1")
fd2 = open("./pipe2")

poll = select.poll()
poll.register(fd1)
poll.register(fd2)

while True:
	events = poll.poll()

	for fd, event in events:
		if event == select.POLLIN or event == select.POLLPRI:
			print(event)
			print(os.read(fd, 1000))

		# fixme: proper error handling
		if event == select.POLLERR:
			print("error on: " + fd)

# fixme: close files