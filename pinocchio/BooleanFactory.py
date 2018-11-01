from .ReqFactory import ReqFactory
from .TraceType import BOOLEAN_TYPE
from .DFG import CmpLT, CmpLEQ, Constant, Add, Subtract, Multiply, Negate,Input, Conditional
from .BusReq import ConstantReq
from .ArithBusReq import NegateReq
from .BooleanBuses import BooleanZero, BooleanOutputBus, ConstantBitXorBus, AllOnesBus, BitAndBus, BitOrBus, XorBus
from .BooleanBusReq import BooleanInputReq, AddReq, CmpReq, ConditionalReq, MultiplyReq


class BooleanFactory(ReqFactory):
	def __init__(self, output_filename, circuit_inputs, circuit_outputs, bit_width):
		ReqFactory.__init__(self, output_filename, circuit_inputs, circuit_outputs, bit_width)

	def type(self):
		return BOOLEAN_TYPE

	def make_zero_bus(self):
		return BooleanZero(self.get_board())

	def make_input_req(self, expr):
		return BooleanInputReq(self, expr, self.type())

	def make_output_bus(self, expr_bus, idx):
		return BooleanOutputBus(self.get_board(), expr_bus, idx)

	def make_req(self, expr, type):
		assert type==BOOLEAN_TYPE
		if isinstance(expr, Input):
			return BooleanInputReq(self, expr, type)
		elif isinstance(expr, Conditional):
			return ConditionalReq(self, expr, type)
		elif isinstance(expr, CmpLT):
			return CmpReq(self, expr, type)
		elif isinstance(expr, CmpLEQ):
			return CmpReq(self, expr, type)
		elif isinstance(expr, Constant):
			return ConstantReq(self, expr, type)
		elif isinstance(expr, Add):
			return AddReq(self, expr, type)
		elif isinstance(expr, Subtract):
			return SubtractReq(self, expr, type)
		elif isinstance(expr, Multiply):
			return MultiplyReq(self, expr, type)
		elif isinstance(expr, Negate):
			return NegateReq(self, expr, type)
		else:
			return ReqFactory.make_req(self, expr, type)

	def collapse_req(self, req):
		return req.natural_impl()

	def get_BitAndBus_class(self):
		return BitAndBus

	def get_BitOrBus_class(self):
		return BitOrBus

	def get_XorBus_class(self):
		return XorBus

	def get_ConstantBitXorBus_class(self):
		return ConstantBitXorBus

	def get_AllOnesBus_class(self):
		return AllOnesBus
