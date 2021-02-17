#include "gtest/gtest.h"
#include "calc.h"
TEST(testADD, test1){
    EXPECT_EQ(5, Calc::add(2,3));
}