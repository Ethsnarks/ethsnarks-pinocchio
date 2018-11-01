#pragma once

struct Input {
	int a;
	int b;
};

struct Output {
	int test_add;
	int test_sub;
	int test_mul;
	int test_or;
	int test_xor;
	int test_and;
};

void outsource(struct Input *input, struct Output *output);
