import cv2
import pyautogui

def main():
    # Inicializa a captura de vídeo
    cap = cv2.VideoCapture(0)  # 0 para câmera padrão, você pode ajustar caso tenha mais de uma câmera

    while True:
        # Lê o frame da captura de vídeo
        ret, frame = cap.read()

        # Converte a imagem para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Realiza o rastreamento de mãos usando a biblioteca pyautogui
        hand_positions = pyautogui.locateAllOnScreen(gray, confidence=0.8)  # Ajuste a confiança conforme necessário

        # Desenha um retângulo em torno de cada posição de mão encontrada
        for hand_pos in hand_positions:
            x, y, width, height = hand_pos
            cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 2)

        # Exibe o frame com os retângulos das mãos
        cv2.imshow('Hand Tracking', frame)

        # Verifica se a tecla 'q' foi pressionada para sair
        if cv2.waitKey(1) == ord('q'):  # Encerra o loop se a tecla 'q' for pressionada
            break

    # Libera os recursos
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
