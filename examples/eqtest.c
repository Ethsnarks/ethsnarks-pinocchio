#include "eqtest-ifc.h"

void outsource(struct Input *input, struct Output *output)
{
	output->y = (input->a + 5);
	output->z = (input->b * 2);
	output->x = output->y == output->z;
}
