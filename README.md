# RnD_FSODforAI: Few-Shot Object Detection (FSOD) cho Ảnh Chụp trên Không

## 1. Giới thiệu

Đây là bài làm của ứng viên **Nhan Hữu Hiếu** cho bài kiểm tra năng lực đầu vào - Vị trí **Kỹ sư R&D CT UAV**.

Dự án này tập trung vào việc nghiên cứu và triển khai giải pháp **Phát hiện Đối tượng Ít Mẫu (Few-Shot Object Detection - FSOD)**, đặc biệt tối ưu cho các vật thể nhỏ và có sự biến đổi cao trong **ảnh chụp từ trên không (Aerial Imagery)**, nhằm đánh giá khả năng áp dụng các kỹ thuật học sâu tiên tiến (như Meta-Learning và Contrastive Learning) vào bài toán thực tế của CT UAV.

---

## 2. Cấu trúc Thư mục Dự án

Cấu trúc thư mục gốc của dự án được tổ chức như sau:
RnD_FSODforAI/ 

    ├── dataset/
    
        ├── test/ 
        
            ├── images/ 
            
            └── annotations/ 
            
        └── train/  
        
            ├── images/ 
            
            └── annotations/ 
            
    ├── src/ 
    
        ├── RnD_FSODforAI.ipynb (Chứa mã nguồn chính của mô hình, v.v.) 
        
        └── prepare_data.py
        
    ├── others/ 
    
    ├── CTUAV_RNDTest_NHHieu_Report.pdf 
    
    └── README.md

## 3. Hướng dẫn Chạy và Thử nghiệm

File `prepare_data.py` dùng để chuyển đổi các file annotations gốc của DOTA thành format mà mô hình fine-tune hiểu được.
Các file annotations này đã được chuẩn hóa sẵn nên không cần chuẩn hóa lại.
Để tái tạo môi trường và chạy thử nghiệm mô hình, vui lòng thực hiện theo các bước sau:

### 3.1. Tải về và upload dữ liệu huấn luyện

- Tải đủ folder dataset và upload lại dữ liệu này lên Google Drive (vì cần sử dụng Google Colab để chạy).

- Lưu lại đường dẫn nơi lưu dataset này.

### 3.2 Tải file code lên Google Colab để chạy

- Tải RnD_FSODforAI.ipynb và mở bằng Google Colab.

- Đổi đường dẫn ROOT (trong file .ipynb) thành đường dẫn dùng để lưu project trên Google Drive.

- Cấp quyền truy cập vào Google Drive cho Colab.

- Chạy hết các cell code còn lại.

## 4. Liên hệ

Mọi thắc mắc hoặc cần làm rõ thêm về mã nguồn và báo cáo kỹ thuật, vui lòng liên hệ:

Ứng viên: Nhan Hữu Hiếu

Email: nhanhuuhieu@gmail.com

SĐT: 094.522.6012
