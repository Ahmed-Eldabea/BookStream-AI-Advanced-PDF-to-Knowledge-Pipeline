import fitz  # PyMuPDF
import os

def compress_pdf(input_path, output_path):
    """
    نسخة مطورة متوافقة مع الإصدارات الحديثة لضغط الـ PDF.
    """
    if not os.path.exists(input_path):
        print(f"❌ الخطأ: الملف {input_path} غير موجود!")
        return

    print(f"🗜️ جاري ضغط الملف: {input_path}...")
    
    try:
        # فتح الملف
        doc = fitz.open(input_path)
        
        # إعدادات الحفظ المتوافقة مع الإصدارات الجديدة
        # حذفنا linear=True لتجنب الخطأ code=4
        doc.save(output_path, 
                 garbage=4, 
                 deflate=True, 
                 clean=True)
        
        doc.close()

        # حساب النتائج
        initial_size = os.path.getsize(input_path) / (1024 * 1024)
        final_size = os.path.getsize(output_path) / (1024 * 1024)
        
        print(f"✅ تم الضغط بنجاح!")
        print(f"📊 الحجم قبل: {initial_size:.2f} MB")
        print(f"📉 الحجم بعد: {final_size:.2f} MB")
        print(f"🚀 تم تقليص الحجم بنسبة: {((initial_size - final_size) / initial_size) * 100:.1f}%")

    except Exception as e:
        print(f"❌ حدث خطأ غير متوقع: {e}")

if __name__ == "__main__":
    # تأكد من أن الاسم مطابق لملفك الموجود في المجلد
    input_file = "Ophthalmology-book.pdf"
    output_file = "compressed_Ophthalmology.pdf"
    
    compress_pdf(input_file, output_file)