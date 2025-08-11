#!/usr/bin/env python3
"""
Teste independente para verificar disponibilidade de GPU/CUDA para OpenCV
"""

def test_gpu_cuda():
    """Testar disponibilidade e funcionalidade da GPU/CUDA."""
    print("🧪 Testando disponibilidade da GPU/CUDA para OpenCV...")
    
    try:
        import cv2
        print(f"✅ OpenCV {cv2.__version__} instalado")
        
        # Verificar se o módulo CUDA está disponível
        if not hasattr(cv2, 'cuda'):
            print("❌ OpenCV não foi compilado com suporte CUDA")
            print("💡 Para usar GPU, você precisa instalar opencv-python compilado com CUDA")
            print("   Ou usar opencv-contrib-python se disponível com CUDA")
            return False
            
        print("✅ Módulo cv2.cuda encontrado")
        
        # Verificar dispositivos CUDA
        try:
            cuda_devices = cv2.cuda.getCudaEnabledDeviceCount()
            if cuda_devices == 0:
                print("❌ Nenhum dispositivo CUDA encontrado")
                print("💡 Verifique se:")
                print("   - Sua GPU suporta CUDA")
                print("   - Os drivers NVIDIA estão instalados")
                print("   - CUDA toolkit está instalado")
                return False
                
            print(f"✅ {cuda_devices} dispositivo(s) CUDA encontrado(s)")
            
            # Obter informações do dispositivo
            for i in range(cuda_devices):
                try:
                    device_info = cv2.cuda.getDevice()
                    print(f"   Dispositivo {i}: Ativo")
                except:
                    print(f"   Dispositivo {i}: Não foi possível obter informações")
                    
        except Exception as e:
            print(f"❌ Erro ao verificar dispositivos CUDA: {e}")
            return False
        
        # Testar operação básica na GPU
        try:
            print("🧪 Testando operações básicas na GPU...")
            import numpy as np
            
            # Criar uma matriz teste pequena
            test_mat = np.random.randint(0, 255, (100, 100), dtype=np.uint8)
            
            # Testar upload/download
            gpu_mat = cv2.cuda_GpuMat()
            gpu_mat.upload(test_mat)
            downloaded = gpu_mat.download()
            
            if np.array_equal(test_mat, downloaded):
                print("✅ Upload/Download GPU funcionando")
            else:
                print("❌ Upload/Download GPU falhou")
                return False
                
        except Exception as gpu_error:
            print(f"❌ Erro em operações básicas GPU: {gpu_error}")
            return False
            
        # Testar template matching na GPU
        try:
            print("🧪 Testando template matching na GPU...")
            
            # Criar imagem e template de teste
            test_image = np.random.randint(0, 255, (200, 200), dtype=np.uint8)
            template = test_image[50:100, 50:100]  # Extrair um pedaço como template
            
            # Upload para GPU
            gpu_image = cv2.cuda_GpuMat()
            gpu_template = cv2.cuda_GpuMat()
            gpu_image.upload(test_image)
            gpu_template.upload(template)
            
            # Criar matcher
            matcher = cv2.cuda.createTemplateMatching(gpu_image.type(), cv2.TM_CCOEFF_NORMED)
            gpu_result = matcher.match(gpu_image, gpu_template)
            result = gpu_result.download()
            
            if result is not None and result.size > 0:
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                print("✅ Template matching na GPU funcional!")
                print(f"   Melhor match: {max_val:.3f} na posição {max_loc}")
                print("🚀 GPU está pronta para uso no puzzle solver!")
                return True
            else:
                print("❌ Template matching na GPU falhou - resultado vazio")
                return False
                
        except Exception as match_error:
            print(f"❌ Erro no template matching GPU: {match_error}")
            return False
            
    except ImportError:
        print("❌ OpenCV não está instalado")
        print("💡 Instale com: pip install opencv-python")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

if __name__ == "__main__":
    success = test_gpu_cuda()
    if success:
        print("\n🎉 GPU/CUDA está funcionando perfeitamente!")
        print("Você pode usar a opção GPU no puzzle solver.")
    else:
        print("\n⚠️ GPU/CUDA não está funcionando.")
        print("Use apenas CPU no puzzle solver.")
