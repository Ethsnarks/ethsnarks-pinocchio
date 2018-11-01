#include "optests-ifc.h"

void outsource(struct Input *input, struct Output *output)
{
	output->test_add = input->a + input->b;
	output->test_sub = input->a - input->b;
	output->test_mul = input->a * input->b;
	output->test_or  = input->a | input->b;
	output->test_xor = input->a ^ input->b;
	output->test_and = input->a & input->b;
}