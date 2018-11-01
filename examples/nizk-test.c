#include "nizk-test-ifc.h"


void outsource(struct Input *input, struct NIZKInput *nizkinput, struct Output *output)
{
	output->c1 = input->a + nizkinput->b1;
	output->c3 = input->a + nizkinput->b3;
}
