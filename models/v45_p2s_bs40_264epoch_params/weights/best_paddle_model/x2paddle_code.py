import paddle
import math
from x2paddle.op_mapper.pytorch2paddle import pytorch_custom_layer as x2paddle_nn

class DetectionModel(paddle.nn.Layer):
    def __init__(self):
        super(DetectionModel, self).__init__()
        self.conv2d0 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=32, kernel_size=(3, 3), in_channels=3)
        self.silu0 = paddle.nn.Silu()
        self.conv2d1 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=64, kernel_size=(3, 3), in_channels=32)
        self.silu1 = paddle.nn.Silu()
        self.conv2d2 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=64)
        self.silu2 = paddle.nn.Silu()
        self.conv2d3 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=32)
        self.silu3 = paddle.nn.Silu()
        self.conv2d4 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=32)
        self.silu4 = paddle.nn.Silu()
        self.conv2d5 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=96)
        self.silu5 = paddle.nn.Silu()
        self.conv2d6 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=128, kernel_size=(3, 3), in_channels=64)
        self.silu6 = paddle.nn.Silu()
        self.conv2d7 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=128)
        self.silu7 = paddle.nn.Silu()
        self.conv2d8 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu8 = paddle.nn.Silu()
        self.conv2d9 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu9 = paddle.nn.Silu()
        self.conv2d10 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu10 = paddle.nn.Silu()
        self.conv2d11 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu11 = paddle.nn.Silu()
        self.conv2d12 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=256)
        self.silu12 = paddle.nn.Silu()
        self.conv2d13 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=256, kernel_size=(3, 3), in_channels=128)
        self.silu13 = paddle.nn.Silu()
        self.conv2d14 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=256)
        self.silu14 = paddle.nn.Silu()
        self.conv2d15 = paddle.nn.Conv2D(padding=1, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu15 = paddle.nn.Silu()
        self.conv2d16 = paddle.nn.Conv2D(padding=1, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu16 = paddle.nn.Silu()
        self.conv2d17 = paddle.nn.Conv2D(padding=1, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu17 = paddle.nn.Silu()
        self.conv2d18 = paddle.nn.Conv2D(padding=1, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu18 = paddle.nn.Silu()
        self.conv2d19 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=512)
        self.silu19 = paddle.nn.Silu()
        self.conv2d20 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=512, kernel_size=(3, 3), in_channels=256)
        self.silu20 = paddle.nn.Silu()
        self.conv2d21 = paddle.nn.Conv2D(out_channels=512, kernel_size=(1, 1), in_channels=512)
        self.silu21 = paddle.nn.Silu()
        self.conv2d22 = paddle.nn.Conv2D(padding=1, out_channels=256, kernel_size=(3, 3), in_channels=256)
        self.silu22 = paddle.nn.Silu()
        self.conv2d23 = paddle.nn.Conv2D(padding=1, out_channels=256, kernel_size=(3, 3), in_channels=256)
        self.silu23 = paddle.nn.Silu()
        self.conv2d24 = paddle.nn.Conv2D(out_channels=512, kernel_size=(1, 1), in_channels=768)
        self.silu24 = paddle.nn.Silu()
        self.conv2d25 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=512)
        self.silu25 = paddle.nn.Silu()
        self.pool2d0 = paddle.nn.MaxPool2D(kernel_size=[5, 5], stride=1, padding=2)
        self.pool2d1 = paddle.nn.MaxPool2D(kernel_size=[5, 5], stride=1, padding=2)
        self.pool2d2 = paddle.nn.MaxPool2D(kernel_size=[5, 5], stride=1, padding=2)
        self.conv2d26 = paddle.nn.Conv2D(out_channels=512, kernel_size=(1, 1), in_channels=1024)
        self.silu26 = paddle.nn.Silu()
        self.conv2d27 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=768)
        self.silu27 = paddle.nn.Silu()
        self.conv2d28 = paddle.nn.Conv2D(padding=1, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu28 = paddle.nn.Silu()
        self.conv2d29 = paddle.nn.Conv2D(padding=1, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu29 = paddle.nn.Silu()
        self.conv2d30 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=384)
        self.silu30 = paddle.nn.Silu()
        self.conv2d31 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=384)
        self.silu31 = paddle.nn.Silu()
        self.conv2d32 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu32 = paddle.nn.Silu()
        self.conv2d33 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu33 = paddle.nn.Silu()
        self.conv2d34 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=192)
        self.silu34 = paddle.nn.Silu()
        self.conv2d35 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=192)
        self.silu35 = paddle.nn.Silu()
        self.conv2d36 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=32)
        self.silu36 = paddle.nn.Silu()
        self.conv2d37 = paddle.nn.Conv2D(padding=1, out_channels=32, kernel_size=(3, 3), in_channels=32)
        self.silu37 = paddle.nn.Silu()
        self.conv2d38 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=96)
        self.silu38 = paddle.nn.Silu()
        self.conv2d39 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu39 = paddle.nn.Silu()
        self.conv2d40 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=192)
        self.silu40 = paddle.nn.Silu()
        self.conv2d41 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu41 = paddle.nn.Silu()
        self.conv2d42 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu42 = paddle.nn.Silu()
        self.conv2d43 = paddle.nn.Conv2D(out_channels=128, kernel_size=(1, 1), in_channels=192)
        self.silu43 = paddle.nn.Silu()
        self.conv2d44 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu44 = paddle.nn.Silu()
        self.conv2d45 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=384)
        self.silu45 = paddle.nn.Silu()
        self.conv2d46 = paddle.nn.Conv2D(padding=1, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu46 = paddle.nn.Silu()
        self.conv2d47 = paddle.nn.Conv2D(padding=1, out_channels=128, kernel_size=(3, 3), in_channels=128)
        self.silu47 = paddle.nn.Silu()
        self.conv2d48 = paddle.nn.Conv2D(out_channels=256, kernel_size=(1, 1), in_channels=384)
        self.silu48 = paddle.nn.Silu()
        self.conv2d49 = paddle.nn.Conv2D(stride=2, padding=1, out_channels=256, kernel_size=(3, 3), in_channels=256)
        self.silu49 = paddle.nn.Silu()
        self.conv2d50 = paddle.nn.Conv2D(out_channels=512, kernel_size=(1, 1), in_channels=768)
        self.silu50 = paddle.nn.Silu()
        self.conv2d51 = paddle.nn.Conv2D(padding=1, out_channels=256, kernel_size=(3, 3), in_channels=256)
        self.silu51 = paddle.nn.Silu()
        self.conv2d52 = paddle.nn.Conv2D(padding=1, out_channels=256, kernel_size=(3, 3), in_channels=256)
        self.silu52 = paddle.nn.Silu()
        self.conv2d53 = paddle.nn.Conv2D(out_channels=512, kernel_size=(1, 1), in_channels=768)
        self.silu53 = paddle.nn.Silu()
        self.x764 = self.create_parameter(dtype='float32', shape=(1, 34000), default_initializer=paddle.nn.initializer.Constant(value=0.0))
        self.conv2d54 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu54 = paddle.nn.Silu()
        self.conv2d55 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu55 = paddle.nn.Silu()
        self.conv2d56 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=64)
        self.conv2d57 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu56 = paddle.nn.Silu()
        self.conv2d58 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu57 = paddle.nn.Silu()
        self.conv2d59 = paddle.nn.Conv2D(out_channels=1, kernel_size=(1, 1), in_channels=64)
        self.conv2d60 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=128)
        self.silu58 = paddle.nn.Silu()
        self.conv2d61 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu59 = paddle.nn.Silu()
        self.conv2d62 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=64)
        self.conv2d63 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=128)
        self.silu60 = paddle.nn.Silu()
        self.conv2d64 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu61 = paddle.nn.Silu()
        self.conv2d65 = paddle.nn.Conv2D(out_channels=1, kernel_size=(1, 1), in_channels=64)
        self.conv2d66 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=256)
        self.silu62 = paddle.nn.Silu()
        self.conv2d67 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu63 = paddle.nn.Silu()
        self.conv2d68 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=64)
        self.conv2d69 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=256)
        self.silu64 = paddle.nn.Silu()
        self.conv2d70 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu65 = paddle.nn.Silu()
        self.conv2d71 = paddle.nn.Conv2D(out_channels=1, kernel_size=(1, 1), in_channels=64)
        self.conv2d72 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=512)
        self.silu66 = paddle.nn.Silu()
        self.conv2d73 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu67 = paddle.nn.Silu()
        self.conv2d74 = paddle.nn.Conv2D(out_channels=64, kernel_size=(1, 1), in_channels=64)
        self.conv2d75 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=512)
        self.silu68 = paddle.nn.Silu()
        self.conv2d76 = paddle.nn.Conv2D(padding=1, out_channels=64, kernel_size=(3, 3), in_channels=64)
        self.silu69 = paddle.nn.Silu()
        self.conv2d77 = paddle.nn.Conv2D(out_channels=1, kernel_size=(1, 1), in_channels=64)
        self.softmax0 = paddle.nn.Softmax(axis=1)
        self.conv2d78 = paddle.nn.Conv2D(out_channels=1, kernel_size=(1, 1), bias_attr=False, in_channels=16)
        self.x1047 = self.create_parameter(dtype='float32', shape=(1, 2, 34000), default_initializer=paddle.nn.initializer.Constant(value=0.0))
        self.sigmoid0 = paddle.nn.Sigmoid()

    def forward(self, x0):
        x51 = self.conv2d0(x0)
        x52 = self.silu0(x51)
        x63 = self.conv2d1(x52)
        x64 = self.silu1(x63)
        x79 = self.conv2d2(x64)
        x80 = self.silu2(x79)
        x82 = paddle.split(x=x80, num_or_sections=2, axis=1)
        x83, x84 = x82
        x94 = self.conv2d3(x84)
        x95 = self.silu3(x94)
        x103 = self.conv2d4(x95)
        x104 = self.silu4(x103)
        x105 = x84 + x104
        x106 = [x83, x84, x105]
        x107 = paddle.concat(x=x106, axis=1)
        x115 = self.conv2d5(x107)
        x116 = self.silu5(x115)
        x127 = self.conv2d6(x116)
        x128 = self.silu6(x127)
        x145 = self.conv2d7(x128)
        x146 = self.silu7(x145)
        x148 = paddle.split(x=x146, num_or_sections=2, axis=1)
        x149, x150 = x148
        x160 = self.conv2d8(x150)
        x161 = self.silu8(x160)
        x169 = self.conv2d9(x161)
        x170 = self.silu9(x169)
        x171 = x150 + x170
        x181 = self.conv2d10(x171)
        x182 = self.silu10(x181)
        x190 = self.conv2d11(x182)
        x191 = self.silu11(x190)
        x192 = x171 + x191
        x193 = [x149, x150, x171, x192]
        x194 = paddle.concat(x=x193, axis=1)
        x202 = self.conv2d12(x194)
        x203 = self.silu12(x202)
        x214 = self.conv2d13(x203)
        x215 = self.silu13(x214)
        x232 = self.conv2d14(x215)
        x233 = self.silu14(x232)
        x235 = paddle.split(x=x233, num_or_sections=2, axis=1)
        x236, x237 = x235
        x247 = self.conv2d15(x237)
        x248 = self.silu15(x247)
        x256 = self.conv2d16(x248)
        x257 = self.silu16(x256)
        x258 = x237 + x257
        x268 = self.conv2d17(x258)
        x269 = self.silu17(x268)
        x277 = self.conv2d18(x269)
        x278 = self.silu18(x277)
        x279 = x258 + x278
        x280 = [x236, x237, x258, x279]
        x281 = paddle.concat(x=x280, axis=1)
        x289 = self.conv2d19(x281)
        x290 = self.silu19(x289)
        x301 = self.conv2d20(x290)
        x302 = self.silu20(x301)
        x317 = self.conv2d21(x302)
        x318 = self.silu21(x317)
        x320 = paddle.split(x=x318, num_or_sections=2, axis=1)
        x321, x322 = x320
        x332 = self.conv2d22(x322)
        x333 = self.silu22(x332)
        x341 = self.conv2d23(x333)
        x342 = self.silu23(x341)
        x343 = x322 + x342
        x344 = [x321, x322, x343]
        x345 = paddle.concat(x=x344, axis=1)
        x353 = self.conv2d24(x345)
        x354 = self.silu24(x353)
        x367 = self.conv2d25(x354)
        x368 = self.silu25(x367)
        x373 = self.pool2d0(x368)
        x378 = self.pool2d1(x373)
        x383 = self.pool2d2(x378)
        x384 = [x368, x373, x378, x383]
        x385 = paddle.concat(x=x384, axis=1)
        x393 = self.conv2d26(x385)
        x394 = self.silu26(x393)
        x396 = [2.0, 2.0]
        x397 = paddle.nn.functional.interpolate(x=x394, scale_factor=x396, mode='nearest')
        x399 = [x397, x290]
        x400 = paddle.concat(x=x399, axis=1)
        x415 = self.conv2d27(x400)
        x416 = self.silu27(x415)
        x418 = paddle.split(x=x416, num_or_sections=2, axis=1)
        x419, x420 = x418
        x430 = self.conv2d28(x420)
        x431 = self.silu28(x430)
        x439 = self.conv2d29(x431)
        x440 = self.silu29(x439)
        x441 = [x419, x420, x440]
        x442 = paddle.concat(x=x441, axis=1)
        x450 = self.conv2d30(x442)
        x451 = self.silu30(x450)
        x453 = [2.0, 2.0]
        x454 = paddle.nn.functional.interpolate(x=x451, scale_factor=x453, mode='nearest')
        x456 = [x454, x203]
        x457 = paddle.concat(x=x456, axis=1)
        x472 = self.conv2d31(x457)
        x473 = self.silu31(x472)
        x475 = paddle.split(x=x473, num_or_sections=2, axis=1)
        x476, x477 = x475
        x487 = self.conv2d32(x477)
        x488 = self.silu32(x487)
        x496 = self.conv2d33(x488)
        x497 = self.silu33(x496)
        x498 = [x476, x477, x497]
        x499 = paddle.concat(x=x498, axis=1)
        x507 = self.conv2d34(x499)
        x508 = self.silu34(x507)
        x510 = [2.0, 2.0]
        x511 = paddle.nn.functional.interpolate(x=x508, scale_factor=x510, mode='nearest')
        x513 = [x511, x116]
        x514 = paddle.concat(x=x513, axis=1)
        x529 = self.conv2d35(x514)
        x530 = self.silu35(x529)
        x532 = paddle.split(x=x530, num_or_sections=2, axis=1)
        x533, x534 = x532
        x544 = self.conv2d36(x534)
        x545 = self.silu36(x544)
        x553 = self.conv2d37(x545)
        x554 = self.silu37(x553)
        x555 = [x533, x534, x554]
        x556 = paddle.concat(x=x555, axis=1)
        x564 = self.conv2d38(x556)
        x565 = self.silu38(x564)
        x576 = self.conv2d39(x565)
        x577 = self.silu39(x576)
        x579 = [x577, x508]
        x580 = paddle.concat(x=x579, axis=1)
        x595 = self.conv2d40(x580)
        x596 = self.silu40(x595)
        x598 = paddle.split(x=x596, num_or_sections=2, axis=1)
        x599, x600 = x598
        x610 = self.conv2d41(x600)
        x611 = self.silu41(x610)
        x619 = self.conv2d42(x611)
        x620 = self.silu42(x619)
        x621 = [x599, x600, x620]
        x622 = paddle.concat(x=x621, axis=1)
        x630 = self.conv2d43(x622)
        x631 = self.silu43(x630)
        x642 = self.conv2d44(x631)
        x643 = self.silu44(x642)
        x645 = [x643, x451]
        x646 = paddle.concat(x=x645, axis=1)
        x661 = self.conv2d45(x646)
        x662 = self.silu45(x661)
        x664 = paddle.split(x=x662, num_or_sections=2, axis=1)
        x665, x666 = x664
        x676 = self.conv2d46(x666)
        x677 = self.silu46(x676)
        x685 = self.conv2d47(x677)
        x686 = self.silu47(x685)
        x687 = [x665, x666, x686]
        x688 = paddle.concat(x=x687, axis=1)
        x696 = self.conv2d48(x688)
        x697 = self.silu48(x696)
        x708 = self.conv2d49(x697)
        x709 = self.silu49(x708)
        x711 = [x709, x394]
        x712 = paddle.concat(x=x711, axis=1)
        x727 = self.conv2d50(x712)
        x728 = self.silu50(x727)
        x730 = paddle.split(x=x728, num_or_sections=2, axis=1)
        x731, x732 = x730
        x742 = self.conv2d51(x732)
        x743 = self.silu51(x742)
        x751 = self.conv2d52(x743)
        x752 = self.silu52(x751)
        x753 = [x731, x732, x752]
        x754 = paddle.concat(x=x753, axis=1)
        x762 = self.conv2d53(x754)
        x763 = self.silu53(x762)
        x764 = self.x764
        x765 = 2
        x767 = 2
        x768 = 1
        x798 = self.conv2d54(x565)
        x799 = self.silu54(x798)
        x807 = self.conv2d55(x799)
        x808 = self.silu55(x807)
        x815 = self.conv2d56(x808)
        x826 = self.conv2d57(x565)
        x827 = self.silu56(x826)
        x835 = self.conv2d58(x827)
        x836 = self.silu57(x835)
        x843 = self.conv2d59(x836)
        x844 = [x815, x843]
        x845 = paddle.concat(x=x844, axis=1)
        x856 = self.conv2d60(x631)
        x857 = self.silu58(x856)
        x865 = self.conv2d61(x857)
        x866 = self.silu59(x865)
        x873 = self.conv2d62(x866)
        x884 = self.conv2d63(x631)
        x885 = self.silu60(x884)
        x893 = self.conv2d64(x885)
        x894 = self.silu61(x893)
        x901 = self.conv2d65(x894)
        x902 = [x873, x901]
        x903 = paddle.concat(x=x902, axis=1)
        x914 = self.conv2d66(x697)
        x915 = self.silu62(x914)
        x923 = self.conv2d67(x915)
        x924 = self.silu63(x923)
        x931 = self.conv2d68(x924)
        x942 = self.conv2d69(x697)
        x943 = self.silu64(x942)
        x951 = self.conv2d70(x943)
        x952 = self.silu65(x951)
        x959 = self.conv2d71(x952)
        x960 = [x931, x959]
        x961 = paddle.concat(x=x960, axis=1)
        x972 = self.conv2d72(x763)
        x973 = self.silu66(x972)
        x981 = self.conv2d73(x973)
        x982 = self.silu67(x981)
        x989 = self.conv2d74(x982)
        x1000 = self.conv2d75(x763)
        x1001 = self.silu68(x1000)
        x1009 = self.conv2d76(x1001)
        x1010 = self.silu69(x1009)
        x1017 = self.conv2d77(x1010)
        x1018 = [x989, x1017]
        x1019 = paddle.concat(x=x1018, axis=1)
        x1021 = paddle.reshape(x=x845, shape=[1, 65, -1])
        x1023 = paddle.reshape(x=x903, shape=[1, 65, -1])
        x1025 = paddle.reshape(x=x961, shape=[1, 65, -1])
        x1027 = paddle.reshape(x=x1019, shape=[1, 65, -1])
        x1028 = [x1021, x1023, x1025, x1027]
        x1029 = paddle.concat(x=x1028, axis=2)
        x1031 = paddle.split(x=x1029, num_or_sections=[64, 1], axis=1)
        x1032, x1033 = x1031
        x1036 = paddle.reshape(x=x1032, shape=[1, 4, 16, 34000])
        x1037_shape = x1036.shape
        x1037_len = len(x1037_shape)
        x1037_list = []
        for i in range(x1037_len):
            x1037_list.append(i)
        if x767 < 0:
            x767_new = x767 + x1037_len
        else:
            x767_new = x767
        if x768 < 0:
            x768_new = x768 + x1037_len
        else:
            x768_new = x768
        x1037_list[x767_new] = x768_new
        x1037_list[x768_new] = x767_new
        x1037 = paddle.transpose(x=x1036, perm=x1037_list)
        x1038 = self.softmax0(x1037)
        x1044 = self.conv2d78(x1038)
        x1046 = paddle.reshape(x=x1044, shape=[1, 4, 34000])
        x1047 = self.x1047
        x1048 = paddle.split(x=x1046, num_or_sections=2, axis=1)
        x1049, x1050 = x1048
        x1051 = x1047 - x1049
        x1052 = x1047 + x1050
        x1053 = x1051 + x1052
        x1054 = x1053 / x765
        x1055 = x1052 - x1051
        x1056 = [x1054, x1055]
        x1057 = paddle.concat(x=x1056, axis=1)
        x1058 = x1057 * x764
        x1059 = self.sigmoid0(x1033)
        x1060 = [x1058, x1059]
        x1061 = paddle.concat(x=x1060, axis=1)
        return x1061

def main(x0):
    # There are 1 inputs.
    # x0: shape-[1, 3, 640, 640], type-float32.
    paddle.disable_static()
    params = paddle.load(r'/home/matijasukovic_pi5/projects/watchedolives_pi/models/v45_p2s_bs40_264epoch_params/weights/best_paddle_model/model.pdparams')
    model = DetectionModel()
    model.set_dict(params, use_structured_name=True)
    model.eval()
    out = model(x0)
    return out
