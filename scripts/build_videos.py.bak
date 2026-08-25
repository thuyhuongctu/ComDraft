# -*- coding: utf-8 -*-
"""Dựng 8 video: 5 video ôn tập chương + 3 video hướng dẫn thực hành (EC1103 hệ trực tiếp).
Slide PNG + giọng đọc tiếng Việt (Piper) + FFmpeg. Xuất kèm kịch bản để GV thu lại giọng thật."""
import os, subprocess, json

BASE = os.path.dirname(os.path.abspath(__file__))
SLIDES = os.path.join(BASE, "..", "slides")
VOICE = os.path.join(BASE, "..", "..", "video1", "vi_VN-vais1000-medium.onnx")

# mỗi mục: (mã deck, số slide trong file PNG, lời đọc)
VIDEOS = {}

# ============ 5 VIDEO ÔN TẬP CHƯƠNG (3–5 phút) ============
VIDEOS["ON TAP CHUONG 1 - TONG QUAN GIAO TIEP"] = ("c1", [
 (1, """Chào các bạn, đây là video ôn tập nhanh Chương một: Tổng quan về giao tiếp trong kinh doanh. Trong khoảng bốn phút, cô sẽ cùng các bạn hệ thống lại toàn bộ những gì đã học trên lớp, để các bạn tự kiểm tra xem mình đã nắm chắc chưa."""),
 (5, """Trước hết là khái niệm. Giao tiếp là quá trình trao đổi thông tin, tư tưởng, tình cảm giữa con người với con người nhằm đạt được một mục đích nhất định. Còn giao tiếp trong kinh doanh là hoạt động giao tiếp gắn với quá trình kinh doanh: giữa doanh nghiệp với khách hàng, với đối tác, với cơ quan quản lý, và giữa các thành viên trong nội bộ tổ chức. Các bạn nhớ giúp cô: mọi cuộc giao tiếp trong kinh doanh đều hướng tới một mục tiêu công việc cụ thể, chứ không phải trò chuyện ngẫu nhiên."""),
 (6, """Giao tiếp trong kinh doanh có bốn đặc điểm. Một, luôn có mục đích rõ ràng. Hai, đa dạng chủ thể và vai vế: cùng lúc chúng ta giao tiếp với khách hàng, cấp trên, đồng nghiệp, mỗi đối tượng một chuẩn mực riêng. Ba, chịu ràng buộc về lợi ích và pháp lý: lời nói và văn bản có thể tạo ra nghĩa vụ, hợp đồng, trách nhiệm. Và bốn, vừa là khoa học vừa là nghệ thuật: có nguyên tắc để học, nhưng phải vận dụng linh hoạt mới hiệu quả."""),
 (7, """Đây là sơ đồ quan trọng nhất của chương. Quá trình giao tiếp đi qua năm khâu: người gửi hình thành ý tưởng, mã hóa thành lời nói hay chữ viết, thông điệp truyền qua kênh, người nhận giải mã, rồi phản hồi trở lại. Nhiễu có thể xen vào bất cứ khâu nào: tiếng ồn, đường truyền kém, khác biệt ngôn ngữ và văn hóa, định kiến, cảm xúc tiêu cực. Khi một cuộc giao tiếp thất bại, các bạn hãy dò lại từng khâu để tìm xem hỏng ở đâu."""),
 (9, """Về phương tiện, ngoài ngôn ngữ nói và ngôn ngữ viết, chúng ta còn giao tiếp bằng phi ngôn ngữ: ánh mắt, nét mặt, nụ cười, cử chỉ, tư thế, khoảng cách, trang phục, giọng điệu và cả việc đúng giờ. Nghiên cứu của Mehrabian cho thấy với thông điệp mang tính cảm xúc, từ ngữ chỉ chiếm khoảng bảy phần trăm, giọng nói ba mươi tám phần trăm, còn ngôn ngữ cơ thể chiếm tới năm mươi lăm phần trăm. Vì vậy, đừng để cơ thể nói ngược lại với lời của mình."""),
 (12, """Cuối cùng là năm nguyên tắc giao tiếp mà các bạn cần thuộc. Tôn trọng. Thiện chí và hợp tác. Lắng nghe và thấu hiểu trước khi trình bày quan điểm. Phù hợp ngữ cảnh: đúng vai, đúng lúc, đúng nơi, đúng kênh. Và chuẩn mực, giữ chữ tín — chữ tín chính là tài sản kinh doanh."""),
 (14, """Tóm lại ba điều cần nhớ. Thứ nhất, giao tiếp kinh doanh có mục đích và có luật chơi. Thứ hai, hiệu quả được quyết định ở cả năm khâu và ở việc kiểm soát nhiễu. Thứ ba, phi ngôn ngữ mạnh hơn chúng ta tưởng. Các bạn hãy làm bốn mươi câu trắc nghiệm Chương một để tự đánh giá nhé. Hẹn gặp lại các bạn ở video ôn tập Chương hai."""),
])

VIDEOS["ON TAP CHUONG 2 - KY NANG GIAO TIEP CHUYEN NGHIEP"] = ("c2", [
 (1, """Chào các bạn, video ôn tập Chương hai: Các kỹ năng giao tiếp chuyên nghiệp. Chương này có bốn kỹ năng mà các bạn sẽ dùng gần như mỗi ngày trong suốt sự nghiệp của mình."""),
 (4, """Kỹ năng thứ nhất là tạo ấn tượng ban đầu. Hãy nhớ quy tắc bốn nhân hai mươi: hai mươi giây đầu tiên, hai mươi bước chân đầu tiên, hai mươi centimet gương mặt tức là ánh mắt và nụ cười, và hai mươi từ đầu tiên. Ấn tượng ban đầu hình thành gần như tức thì và rất khó đảo ngược, cho nên nó phải được chuẩn bị chứ không phó mặc cho may mắn."""),
 (5, """Đi kèm là các nghi thức xã giao. Chào hỏi: người nhỏ chào người lớn, nhân viên chào cấp trên trước. Bắt tay: đứng dậy, nhìn vào mắt, siết vừa phải hai đến ba giây; người có vị thế cao hơn hoặc phụ nữ chủ động đưa tay trước. Danh thiếp: trao và nhận bằng hai tay, mặt chữ hướng về người nhận, đọc qua rồi mới cất, đừng nhét ngay vào túi quần."""),
 (7, """Kỹ năng thứ hai là thuyết trình. Chuẩn bị theo năm bước: phân tích người nghe, xác định mục tiêu, xây dựng nội dung với tối đa ba ý chính, thiết kế slide ít chữ nhiều hình, và luyện tập. Cấu trúc bài nói gồm mở đầu chiếm mười đến mười lăm phần trăm, thân bài bảy mươi đến tám mươi phần trăm, và kết luận mười đến mười lăm phần trăm. Nhớ giúp cô: nói với người nghe, đừng nói với slide."""),
 (9, """Kỹ năng thứ ba là lắng nghe. Có năm mức độ: phớt lờ, giả vờ nghe, nghe chọn lọc, nghe chăm chú, và cao nhất là nghe thấu cảm — hiểu được cả cảm xúc và nhu cầu đằng sau lời nói. Lắng nghe chủ động nghĩa là không ngắt lời, không vội phán xét, ghi chú ý chính, và diễn đạt lại để xác nhận: nếu em hiểu đúng thì ý anh chị là gì."""),
 (11, """Kỹ năng thứ tư là giao tiếp qua điện thoại. Cuộc gọi đi có bốn bước: chuẩn bị trước, mở đầu đúng nghi thức bằng cách chào, xưng danh và xin phép, trình bày gọn rồi tóm tắt lại thỏa thuận, và kết thúc lịch sự. Khi nghe máy, hãy nhấc trong khoảng ba hồi chuông, chào và xưng danh đơn vị. Người gọi nghe thấy được nụ cười của bạn qua giọng nói đấy."""),
 (14, """Ba điều cần nhớ của chương. Ấn tượng ban đầu được chuẩn bị chứ không phải may mắn. Thuyết trình hay bắt đầu từ việc hiểu người nghe. Và lắng nghe cùng đặt câu hỏi mới là kỹ năng bán hàng giỏi nhất. Các bạn hoàn thành bốn mươi câu trắc nghiệm Chương hai nhé. Hẹn gặp lại ở Chương ba."""),
])

VIDEOS["ON TAP CHUONG 3 - TINH HUONG DAC THU"] = ("c3", [
 (1, """Chào các bạn, video ôn tập Chương ba: Giao tiếp trong các tình huống đặc thù. Cùng một kỹ năng, nhưng mỗi bối cảnh lại có một luật chơi riêng."""),
 (4, """Trong nội bộ tổ chức, khi nhận nhiệm vụ từ cấp trên: lắng nghe, ghi chú, hỏi lại cho rõ yêu cầu, thời hạn và nguồn lực, rồi xác nhận lại bằng tin nhắn hoặc email để hai bên cùng hiểu một cách. Khi báo cáo: chủ động, đúng hạn, nói kết quả trước rồi mới diễn giải; đặc biệt là báo tin xấu sớm kèm phương án xử lý, đừng che giấu."""),
 (5, """Với cấp dưới, giao việc phải rõ mục tiêu, thời hạn và tiêu chuẩn. Nguyên tắc vàng khi đánh giá: khen công khai, kịp thời và cụ thể; phê bình riêng tư, nhắm vào hành vi chứ không nhắm vào con người, và luôn kèm hướng khắc phục."""),
 (7, """Đây là nội dung quan trọng nhất của chương: quy trình LAST để xử lý phàn nàn của khách hàng. L là Listen, lắng nghe trọn vẹn, không ngắt lời, không phòng thủ. A là Apologize, xin lỗi chân thành về trải nghiệm chưa tốt, kể cả khi lỗi chưa rõ thuộc về ai. S là Solve, đưa phương án cụ thể với thời hạn rõ ràng. Và T là Thank, cảm ơn khách đã phản hồi rồi theo dõi đến khi xong. Một khách hàng phàn nàn được xử lý tốt thường trung thành hơn khách hàng chưa từng gặp vấn đề."""),
 (9, """Trên bàn tiệc, hãy nhớ: đến đúng giờ, chờ chủ tiệc mời và xếp chỗ vì vị trí ngồi thể hiện thứ bậc; dùng dụng cụ từ ngoài vào trong; khi cụng ly, người vị thế thấp hơn nâng ly thấp hơn; tôn trọng người không dùng rượu bia và tuyệt đối không ép. Câu chuyện nên nhẹ nhàng: ẩm thực, thể thao, du lịch; tránh chính trị, tôn giáo, thu nhập và đời tư."""),
 (10, """Trong môi trường đa văn hóa, các bạn cần nhận diện bốn khác biệt: cách nói thẳng hay nói vòng; mức độ coi trọng thứ bậc; quan niệm về thời gian; và các cử chỉ, kiêng kỵ riêng. Ví dụ, câu để chúng tôi xem xét trong văn hóa Nhật Bản rất có thể chính là một lời từ chối lịch sự."""),
 (13, """Ba điều cần nhớ. Nội bộ vững thì đối ngoại mới mạnh. Khách hàng phàn nàn là cơ hội, hãy dùng quy trình LAST. Và với đa văn hóa: tìm hiểu trước, quan sát, thích ứng, tuyệt đối không phán xét theo chuẩn của mình. Mời các bạn làm bốn mươi câu trắc nghiệm Chương ba."""),
])

VIDEOS["ON TAP CHUONG 4 - DAM PHAN TRONG KINH DOANH"] = ("c4", [
 (1, """Chào các bạn, video ôn tập Chương bốn: Đàm phán trong kinh doanh. Đây có lẽ là kỹ năng sinh lời trực tiếp nhất mà các bạn học trong học phần này."""),
 (4, """Đàm phán là quá trình các bên vừa có lợi ích chung, vừa có lợi ích xung đột, cùng trao đổi và thuyết phục để đi đến một thỏa thuận mà các bên chấp nhận được. Bản chất của nó là kép: hợp tác để chiếc bánh tồn tại và lớn lên, nhưng cạnh tranh khi chia chiếc bánh đó. Ba nguồn sức mạnh trên bàn đàm phán là thông tin, thời gian và thế lực — tức là ai có nhiều lựa chọn thay thế hơn."""),
 (6, """Có ba kiểu đàm phán. Kiểu mềm coi đối tác như bạn, dễ nhượng bộ để giữ quan hệ nhưng dễ chịu thiệt. Kiểu cứng coi đối tác như đối thủ, có thể thắng một lần nhưng phá vỡ quan hệ. Kiểu nguyên tắc, còn gọi là kiểu Harvard, là kiểu chúng ta nên theo: tách con người khỏi vấn đề, tập trung vào lợi ích chứ không cố thủ lập trường, sáng tạo phương án cùng có lợi, và dựa trên tiêu chí khách quan."""),
 (7, """Tiến trình đàm phán gồm năm giai đoạn: chuẩn bị, mở đầu, thương lượng, kết thúc, và sau đàm phán. Trong đó riêng giai đoạn chuẩn bị đã quyết định khoảng bảy mươi phần trăm kết quả. Không chuẩn bị chính là chuẩn bị để nhượng bộ."""),
 (8, """Ba khái niệm phải thuộc. Mục tiêu ba mức: lý tưởng, kỳ vọng và tối thiểu, tức ranh giới rút lui — hãy viết ra giấy trước khi vào bàn. BATNA là phương án thay thế tốt nhất nếu không đạt được thỏa thuận; BATNA càng mạnh thì thế đàm phán càng vững. Và ZOPA là vùng thỏa thuận khả dĩ, tức khoảng chồng lấn giữa giới hạn của hai bên. Nếu không có ZOPA, đừng cố ép giá, hãy mở rộng chiếc bánh bằng cách đổi số lượng, tiến độ hay dịch vụ kèm theo."""),
 (12, """Trên bàn đàm phán, các bạn sẽ gặp một số chiêu trò: neo giá sốc, người tốt kẻ xấu, thời hạn chót giả, cắt lát salami tức đòi thêm từng chút một sau khi đã thỏa thuận, và đòi hỏi phút chót ngay trước khi ký. Cách ứng phó chung là bám vào tiêu chí khách quan, gói toàn bộ điều khoản lại với nhau, và luôn định giá mọi yêu cầu để đòi đối ứng tương xứng."""),
 (14, """Ba điều cần nhớ. Đàm phán thắng từ trước khi ngồi vào bàn. Hãy đàm phán về lợi ích, đừng cố thủ lập trường. Và thỏa thuận chỉ an toàn khi được văn bản hóa thành hợp đồng đúng thể thức — đó chính là nội dung Chương năm. Mời các bạn làm bốn mươi câu trắc nghiệm Chương bốn."""),
])

VIDEOS["ON TAP CHUONG 5 - SOAN THAO VA TRINH BAY VAN BAN"] = ("c5", [
 (1, """Chào các bạn, video ôn tập Chương năm: Soạn thảo và trình bày văn bản. Đây là chương biến mọi thỏa thuận bằng lời thành văn bản có giá trị pháp lý."""),
 (4, """Theo Nghị định ba mươi năm hai nghìn không trăm hai mươi của Chính phủ về công tác văn thư: văn bản là thông tin thành văn được truyền đạt bằng ngôn ngữ hoặc ký hiệu, hình thành trong hoạt động của các cơ quan, tổ chức và được trình bày đúng thể thức, kỹ thuật theo quy định. Có bốn nhóm văn bản: quy phạm pháp luật, hành chính, chuyên ngành và thương mại."""),
 (6, """Về nội dung, văn bản phải đạt bốn yêu cầu: đúng mục đích và đúng thẩm quyền; chính xác, khách quan; rõ ràng, ngắn gọn, dễ hiểu; và đúng pháp luật, đúng ngôn ngữ hành chính, tuyệt đối không dùng khẩu ngữ."""),
 (7, """Đây là sơ đồ các bạn cần chụp lại: chín thành phần thể thức trên trang A bốn. Quốc hiệu và Tiêu ngữ ở góc trên bên phải. Tên cơ quan ban hành ở góc trên bên trái, bên dưới là số và ký hiệu. Địa danh và thời gian ban hành nằm dưới Tiêu ngữ. Tên loại và trích yếu ở giữa. Rồi đến nội dung. Chức vụ, họ tên và chữ ký ở góc dưới bên phải, kèm dấu của cơ quan. Còn nơi nhận ở góc dưới bên trái. Lưu ý riêng: công văn không có tên loại, trích yếu bắt đầu bằng chữ vờ trên gạch chéo vờ."""),
 (8, """Những con số về kỹ thuật trình bày phải thuộc: khổ giấy A bốn; lề trên và lề dưới hai mươi đến hai mươi lăm mi li mét; lề trái ba mươi đến ba mươi lăm mi li mét để đóng gáy lưu trữ; lề phải mười lăm đến hai mươi mi li mét. Phông chữ Times New Roman, bộ mã Unicode, cỡ mười ba đến mười bốn, màu đen. Số trang đánh từ trang thứ hai, bằng chữ số Ả Rập, canh giữa theo lề trên."""),
 (11, """Về văn bản hành chính, các bạn nhớ đặc trưng từng loại: quyết định trình bày theo các Điều, điều cuối ghi hiệu lực thi hành. Tờ trình có ba phần: lý do, phương án, kiến nghị. Công văn không có tên loại và mỗi công văn chỉ nên một chủ đề. Biên bản phải lập ngay tại chỗ và có chữ ký các bên. Báo cáo theo mạch bốn phần: tình hình, kết quả, hạn chế, phương hướng."""),
 (13, """Với văn bản thương mại: thư tín cần đạt nguyên tắc năm C là rõ, gọn, đúng, đủ và lịch sự. Báo giá bắt buộc phải ghi thời hạn hiệu lực. Hợp đồng cần đủ các điều khoản cơ bản, và một thương vụ chỉ trọn vẹn khi có đủ bộ ba: hợp đồng, biên bản nghiệm thu và biên bản thanh lý."""),
 (15, """Ba điều cần nhớ. Thể thức là giấy thông hành của văn bản. Mỗi loại văn bản có một bố cục riêng. Và văn bản thương mại giữ uy tín cho doanh nghiệp. Mời các bạn làm bốn mươi câu trắc nghiệm Chương năm, rồi chuẩn bị cho ba bài thực hành tại phòng máy."""),
])

# ============ 3 VIDEO HƯỚNG DẪN THỰC HÀNH ============
VIDEOS["HUONG DAN THUC HANH BAI 1 - THE THUC VAN BAN"] = ("th1", [
 (1, """Chào các bạn, đây là video hướng dẫn Bài thực hành số một: Thể thức văn bản. Các bạn nên xem video này trước khi đến phòng máy, và có thể mở lại trong lúc làm bài."""),
 (4, """Buổi thực hành diễn ra theo năm bước: cô làm mẫu trên máy chiếu, các bạn thao tác theo, sau đó tự làm bài được giao, chấm chéo theo cặp, rồi nộp và chỉnh sửa. Các bạn nhớ mang laptop có cài Microsoft Word và tải sẵn Nghị định ba mươi."""),
 (5, """Bước một: thiết lập trang giấy. Vào thẻ Layout, chọn Size, chọn A bốn — tuyệt đối không để khổ Letter. Vẫn ở thẻ Layout, chọn Margins rồi Custom Margins: lề trên và dưới đặt hai mươi đến hai mươi lăm mi li mét, lề trái ba mươi đến ba mươi lăm, lề phải mười lăm đến hai mươi. Phông chữ chọn Times New Roman, cỡ mười ba hoặc mười bốn, màu đen. Đánh số trang bằng Insert, Page Number, Top of Page, Center, rồi tích Different First Page để bỏ số ở trang đầu."""),
 (6, """Bước hai: trình bày phần đầu văn bản. Quốc hiệu viết hoa in đậm, Tiêu ngữ in đậm với các chữ cái đầu viết hoa và có gạch nối, bên dưới kẻ một đường ngang. Tên cơ quan ban hành đặt ở góc trên bên trái, cũng có đường kẻ ngang bên dưới. Số và ký hiệu nằm dưới tên cơ quan. Địa danh và thời gian ban hành in nghiêng, đặt dưới Tiêu ngữ; lưu ý ngày nhỏ hơn mười và tháng nhỏ hơn mười phải thêm số không phía trước."""),
 (7, """Bước ba: phần giữa và cuối. Tên loại và trích yếu canh giữa, viết hoa in đậm. Nội dung canh đều hai bên, lùi đầu dòng khoảng một đến một phẩy hai mươi bảy centimet. Phần chữ ký ở góc dưới bên phải: ghi quyền hạn và chức vụ viết hoa, chừa ba đến bốn dòng trống cho chữ ký, rồi họ tên đầy đủ in đậm. Nơi nhận ở góc dưới bên trái, dòng cuối luôn là gạch đầu dòng Lưu hai chấm Vê Tê."""),
 (8, """Trước khi nộp, các bạn hãy tự soát theo bảng kiểm tám điểm này: khổ giấy và lề, phông chữ đồng nhất, Quốc hiệu và Tiêu ngữ, số ký hiệu, ngày tháng và địa danh, trích yếu, chỗ ký và chức vụ, cuối cùng là nơi nhận có dòng Lưu Vê Tê chưa. Đây chính là bảng cô dùng để chấm bài của các bạn."""),
 (9, """Bài nộp số một: trình bày hoàn chỉnh phần thể thức của một Thông báo do Công ty trách nhiệm hữu hạn An Phát ban hành, thông báo lịch nghỉ Tết Nguyên đán cho toàn thể nhân viên. Phần thân chỉ cần ba đến năm dòng, vì trọng tâm chấm là thể thức. Làm cá nhân, nộp file Word cuối buổi. Chúc các bạn làm bài tốt."""),
])

VIDEOS["HUONG DAN THUC HANH BAI 2 - VAN BAN HANH CHINH"] = ("th2", [
 (1, """Chào các bạn, video hướng dẫn Bài thực hành số hai: Soạn thảo văn bản hành chính. Bài này các bạn sẽ soạn năm loại văn bản dùng hằng ngày trong mọi tổ chức."""),
 (5, """Bắt đầu với quyết định. Phần căn cứ viết theo khuôn: Căn cứ văn bản quy định chức năng nhiệm vụ; Căn cứ văn bản chuyên ngành liên quan; Xét đề nghị của đơn vị đề xuất. Mỗi dòng kết thúc bằng dấu chấm phẩy, dòng cuối bằng dấu chấm. Sau đó là chữ QUYẾT ĐỊNH viết hoa in đậm canh giữa, rồi trình bày theo các Điều. Điều cuối luôn ghi hiệu lực thi hành và đối tượng chịu trách nhiệm thi hành. Lỗi hay gặp là dùng từ đề nghị trong quyết định — sai, quyết định phải dùng ngôn ngữ mệnh lệnh."""),
 (6, """Tờ trình gồm ba phần. Mở đầu nêu căn cứ và thực trạng. Nội dung trình bày phương án cụ thể: số lượng, kinh phí dự kiến, thời gian thực hiện, kèm phân tích lợi ích và tính khả thi. Kết thúc bằng câu kính trình cấp có thẩm quyền xem xét, phê duyệt. Đừng quên đính kèm dự toán — đây là lỗi các bạn hay mắc nhất."""),
 (7, """Công văn có đặc điểm nhận diện riêng: không có tên loại. Nghĩa là trên văn bản không có chữ CÔNG VĂN to ở giữa, mà chỉ có số, ký hiệu và dòng trích yếu bắt đầu bằng vờ trên gạch chéo vờ. Công văn đề nghị mở đầu bằng căn cứ và lý do, thân nêu nội dung đề nghị kèm thời hạn, kết thúc bằng Trân trọng chấm gạch chéo chấm. Công văn phúc đáp thì mở đầu bằng: Phúc đáp Công văn số, ngày, của, về việc. Nhớ giúp cô: mỗi công văn chỉ một chủ đề."""),
 (8, """Biên bản và báo cáo. Biên bản mở đầu bằng thời gian, địa điểm, thành phần tham dự; phần thân ghi tuần tự ý kiến từng người một cách ngắn gọn và trung thực; kết thúc bằng kết luận của chủ trì, câu biên bản kết thúc lúc mấy giờ đã đọc lại cho mọi người cùng nghe và thống nhất, rồi chữ ký của thư ký và chủ trì. Người ghi biên bản không được thêm nhận xét chủ quan của mình. Báo cáo thì theo mạch bốn phần: đặc điểm tình hình, kết quả đạt được, hạn chế và nguyên nhân, phương hướng và kiến nghị."""),
 (9, """Bài nộp số hai: từ tình huống Phòng Kế toán Công ty An Phát cần trang bị thêm mười máy tính, mỗi bạn bốc thăm và soạn hai trong năm văn bản: tờ trình, quyết định, công văn, biên bản, báo cáo. Yêu cầu đúng thể thức theo Nghị định ba mươi và đúng bố cục đặc trưng của từng loại. Nộp file Word cuối buổi, rồi chỉnh sửa theo phản hồi của cô trong vòng một tuần."""),
])

VIDEOS["HUONG DAN THUC HANH BAI 3 - VAN BAN THUONG MAI"] = ("th3", [
 (1, """Chào các bạn, video hướng dẫn Bài thực hành số ba: Soạn thảo văn bản thương mại. Bài này các bạn làm theo cặp, một bạn đóng vai bên mua, một bạn đóng vai bên bán."""),
 (5, """Trước hết là thư tín thương mại. Cấu trúc gồm: tiêu đề thư, lời chào, đoạn mở nêu lý do viết thư, đoạn nội dung với thông tin và đề nghị cụ thể, đoạn kết nêu mong muốn và lời cảm ơn, cuối cùng là chữ ký đầy đủ chức danh, đơn vị và thông tin liên hệ. Áp dụng nguyên tắc năm C: mỗi đoạn một ý cho rõ ràng; bỏ câu thừa cho ngắn gọn; đúng tên, chức danh, số liệu; đủ thông tin để bên kia hành động được; và lịch sự ngay cả khi đang khiếu nại."""),
 (6, """Bản báo giá phải có đủ bốn phần. Phần đầu: thông tin doanh nghiệp gồm tên, địa chỉ, mã số thuế, liên hệ; kính gửi khách hàng; số báo giá và ngày lập. Bảng hàng hóa: số thứ tự, tên hàng và quy cách, đơn vị tính, số lượng, đơn giá, thành tiền, thuế giá trị gia tăng, và tổng cộng ghi cả bằng số lẫn bằng chữ. Điều kiện thương mại: thời gian và địa điểm giao hàng, phương thức thanh toán, bảo hành. Và phần cuối là thời hạn hiệu lực báo giá — đừng bao giờ quên phần này, vì giá thị trường luôn biến động."""),
 (7, """Hợp đồng cần đủ các điều khoản cơ bản: thông tin hai bên với người đại diện và tài khoản ngân hàng; Điều một là đối tượng hợp đồng; Điều hai giá trị và phương thức thanh toán; Điều ba thời gian, địa điểm giao hàng và nghiệm thu; Điều bốn quyền và nghĩa vụ mỗi bên kèm bảo hành; Điều năm phạt vi phạm và bồi thường; Điều sáu giải quyết tranh chấp và điều khoản thi hành."""),
 (8, """Sau hợp đồng là hai biên bản khép hồ sơ. Biên bản nghiệm thu ghi rõ căn cứ hợp đồng số mấy, thành phần hai bên, nội dung nghiệm thu tức là chủng loại, số lượng, chất lượng thực nhận so với hợp đồng, rồi kết luận đạt hay không đạt. Biên bản thanh lý xác nhận hai bên đã hoàn thành nghĩa vụ, đối chiếu giá trị đã thanh toán và còn lại, xác nhận chấm dứt hiệu lực hợp đồng."""),
 (9, """Bài nộp số ba: từ chính thương vụ mua hai mươi máy tính đã đàm phán ở Chương bốn, mỗi cặp hoàn thiện bộ hồ sơ đầy đủ. Bên bán soạn thư chào hàng và báo giá. Hai bên cùng dự thảo hợp đồng kèm biên bản nghiệm thu và thanh lý. Sau đó đổi hồ sơ với cặp khác để tìm ít nhất ba điểm bất lợi hoặc thiếu sót. Chúc các bạn thực hành hiệu quả."""),
])


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        raise RuntimeError(" ".join(map(str, cmd))[:120] + "\n" + r.stderr[-700:])
    return r


def build(title, deck, items):
    work = os.path.join(BASE, "_tmp")
    os.makedirs(work, exist_ok=True)
    segs = []
    for i, (slide_no, text) in enumerate(items):
        tpath = os.path.join(work, f"t{i}.txt")
        apath = os.path.join(work, f"a{i}.wav")
        open(tpath, "w", encoding="utf-8").write(text.strip())
        run(["bash", "-c",
             f'piper -m "{VOICE}" --sentence-silence 0.95 --length-scale 1.36 -f "{apath}" < "{tpath}"'])
        img = os.path.join(SLIDES, f"{deck}-{slide_no:02d}.png")
        if not os.path.exists(img):
            img = os.path.join(SLIDES, f"{deck}-{slide_no}.png")
        seg = os.path.join(work, f"s{i}.mp4")
        run(["ffmpeg", "-y", "-loop", "1", "-framerate", "25", "-i", img, "-i", apath,
             "-filter_complex", "[1:a]adelay=900,apad=pad_dur=1.5,aresample=44100[a]",
             "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-tune", "stillimage",
             "-preset", "faster", "-crf", "22", "-pix_fmt", "yuv420p",
             "-ac", "2", "-c:a", "aac", "-b:a", "128k", "-shortest", seg])
        segs.append(seg)
    lst = os.path.join(work, "list.txt")
    open(lst, "w").write("\n".join(f"file '{s}'" for s in segs))
    out = os.path.join(BASE, title + ".mp4")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out])
    d = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                   "-of", "csv=p=0", out]).stdout.strip())
    mb = os.path.getsize(out) / 1e6
    print(f"{title}: {int(d//60)}p{int(d%60):02d}s, {mb:.1f} MB")
    for f in os.listdir(work):
        os.remove(os.path.join(work, f))
    return d


if __name__ == "__main__":
    total = 0
    scripts = {}
    for title, (deck, items) in VIDEOS.items():
        total += build(title, deck, items)
        scripts[title] = [{"slide": n, "loi_doc": t.strip()} for n, t in items]
    json.dump(scripts, open(os.path.join(BASE, "kich_ban_video.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"TỔNG: {len(VIDEOS)} video, {int(total//60)} phút {int(total%60)} giây")
