#pragma once

struct Input {
	int a;
	int b;
};

struct Output {
	int x;
	int y;
	int z;
};

void outsource(struct Input *input, struct Output *output);
