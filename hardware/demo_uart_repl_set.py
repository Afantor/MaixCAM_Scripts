from machine import UART

fm.register(board_info.PIN15,fm.fpioa.UART1_TX)
fm.register(board_info.PIN17,fm.fpioa.UART1_RX)
uart = machine.UART(UART.UART1, 115200)
UART.set_repl_uart(uart)
