#include "stm32f10x.h"                  // Device header

void LED_Init(void)
{
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);
	GPIO_InitTypeDef GPIO_InitStruct;
	GPIO_InitStruct.GPIO_Mode=GPIO_Mode_Out_PP;
	GPIO_InitStruct.GPIO_Pin=GPIO_Pin_1|GPIO_Pin_2;
	GPIO_InitStruct.GPIO_Speed=GPIO_Speed_50MHz;
	GPIO_Init(GPIOA, &GPIO_InitStruct);
	GPIO_SetBits(GPIOA,GPIO_Pin_1|GPIO_Pin_2);
}
void LED1_ON()
{
	GPIO_ResetBits(GPIOA,GPIO_Pin_1);
}
void LED1_OFF()
{
	GPIO_SetBits(GPIOA,GPIO_Pin_1);
}

void LED2_ON()
{
	GPIO_ResetBits(GPIOA,GPIO_Pin_2);
}
void LED2_OFF()
{
	GPIO_SetBits(GPIOA,GPIO_Pin_2);
}


void LED1_Turn(void)
{
	if (GPIO_ReadOutputDataBit(GPIOA, GPIO_Pin_1) == 0)
	{
		GPIO_SetBits(GPIOA, GPIO_Pin_1);
	}
	else
	{
		GPIO_ResetBits(GPIOA, GPIO_Pin_1);
	}
}
void LED2_Turn(void)
{
	if (GPIO_ReadOutputDataBit(GPIOA, GPIO_Pin_11) == 0)
	{
		GPIO_SetBits(GPIOA, GPIO_Pin_11);
	}
	else
	{
		GPIO_ResetBits(GPIOA, GPIO_Pin_11);
	}
}