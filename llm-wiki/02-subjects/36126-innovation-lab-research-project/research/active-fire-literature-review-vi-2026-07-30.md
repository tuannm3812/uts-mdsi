# Tổng quan tài liệu: Phát hiện điểm nóng cháy và giám sát cháy đang hoạt động

**Ngày tổng hợp:** 30 tháng 7 năm 2026

**Mục đích:** Tài liệu tiếng Việt hỗ trợ đọc, thảo luận và chuẩn bị nghiên cứu với TS Arnick Abdollahi

**Phạm vi:** Phát hiện điểm nóng cháy (*fire-hotspot detection*) và giám sát cháy đang hoạt động (*active-fire monitoring*); không nghiên cứu mô phỏng lan truyền đám cháy (*fire-spread modelling*)

## 1. Mục đích, phạm vi và trạng thái bằng chứng

Tài liệu này tổng hợp hai bản tiếng Anh:

- *Preliminary Findings: Fire-Hotspot Detection and Active-Fire Monitoring*; và
- *Active-Fire Research Materials Summary*.

Phạm vi rà soát tài liệu bao gồm Australia và các khu vực khác trên thế giới. Phạm vi mô hình hóa dự kiến được giới hạn ở một bang hoặc tiểu vùng có nguy cơ cháy cao tại Australia, ưu tiên NSW nếu dữ liệu phù hợp.

Tập bằng chứng ban đầu gồm 15 tài liệu hạt giống: 11 công trình có bình duyệt, ba bản tiền ấn phẩm và một báo cáo kỹ thuật của Australia. Một số tài liệu đã có toàn văn, nhưng việc trích xuất toàn văn và truy vết trích dẫn chưa hoàn tất cho toàn bộ tập tài liệu. Vì vậy:

- các mô tả về hệ thống vận hành được kiểm tra từ tài liệu chính thức;
- các kết luận từ bài báo phải tiếp tục được xác minh bằng toàn văn;
- các “khoảng trống nghiên cứu” dưới đây mới là giả thuyết cần kiểm chứng, chưa phải tuyên bố chắc chắn về tính mới.

## 2. Tổng hợp điều hành

Phát hiện cháy đang hoạt động đã có nền tảng tương đối trưởng thành. Các sản phẩm MODIS, VIIRS và vệ tinh địa tĩnh sử dụng thuật toán ngữ cảnh để phát hiện bất thường nhiệt. Australia đã có các hệ thống giám sát đa cảm biến, còn nghiên cứu quốc tế đã áp dụng phân đoạn học sâu, attention, vision transformer, học tự giám sát theo thời gian, hợp nhất đa nguồn và giải thích ngữ nghĩa.

Do đó, các hướng sau **không đủ tính mới nếu đứng riêng lẻ**:

- áp dụng học máy lên ảnh vệ tinh cháy rừng;
- sử dụng transformer để phát hiện cháy;
- kết hợp nhiều sản phẩm vệ tinh;
- tạo biểu đồ SHAP hoặc bản đồ attention;
- thực hiện một nghiên cứu đơn sự kiện tại NSW với cách chia train/test ngẫu nhiên.

Cơ hội nghiên cứu khả thi nhất hiện nay là xây dựng và đánh giá một **lớp độ tin cậy đáng tin cậy** (*trustworthy reliability layer*) cho dữ liệu điểm nóng đa nguồn tại NSW. Nghiên cứu nên tập trung vào:

- kiểm định theo sự kiện và theo thời gian;
- hiệu chỉnh xác suất (*probability calibration*);
- phân tích báo động giả;
- độ bền khi thiếu quan sát hoặc thay đổi cảm biến;
- khả năng tổng quát hóa theo mùa, sự kiện và địa lý; và
- độ ổn định, tính trung thực của lời giải thích.

Mô hình nâng cao—transformer thời gian, mô hình đồ thị hoặc kiến trúc khác—chỉ nên được chọn sau khi hoàn tất kiểm toán dữ liệu và xác nhận khoảng trống.

## 3. Hệ thống vận hành và nền tảng vệ tinh

### 3.1 MODIS và VIIRS

Thuật toán phát hiện cháy ngữ cảnh của MODIS là một đường cơ sở quan trọng. Công trình nền tảng đã cải thiện khả năng phát hiện đám cháy nhỏ hoặc mát hơn và giảm một số báo động giả dai dẳng. MODIS Collection 6 tiếp tục cung cấp sản phẩm cháy toàn cầu lâu dài.

VIIRS cung cấp sản phẩm phát hiện cháy ở độ phân giải 375 m, nhạy hơn với các đám cháy tương đối nhỏ so với sản phẩm MODIS có độ phân giải xấp xỉ 1 km. Tuy nhiên, cả hai đều phụ thuộc vào thời điểm vệ tinh bay qua, bị ảnh hưởng bởi mây, khói và điều kiện quan sát.

Nguồn chính:

- [Thuật toán MODIS ngữ cảnh nâng cao](https://doi.org/10.1016/S0034-4257%2803%2900184-6)
- [MODIS Collection 6](https://doi.org/10.1016/j.rse.2016.02.054)
- [Sản phẩm VIIRS 375 m](https://doi.org/10.1016/j.rse.2013.12.008)
- [Kho dữ liệu NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/active_fire)

### 3.2 Digital Earth Australia Hotspots

[DEA Hotspots](https://knowledge.dea.ga.gov.au/data/product/dea-hotspots/) là dịch vụ vector đa cảm biến trên toàn Australia, có dữ liệu từ ngày 27 tháng 8 năm 2002 đến hiện tại và cập nhật mỗi 10 phút. Các nguồn được mô tả bao gồm MODIS, VIIRS và Himawari/AHI. Thuộc tính có thể bao gồm:

- cảm biến và vệ tinh;
- thuật toán xử lý và phiên bản;
- thời gian thu nhận và xử lý;
- nhiệt độ và công suất bức xạ;
- độ tin cậy;
- độ chính xác vị trí; và
- bang của Australia.

DEA cũng nêu rõ khả năng xuất hiện dương tính giả và âm tính giả. Mây, khói, tán cây, đám cháy nhỏ hoặc mát, thời gian bay qua, gián đoạn cảm biến và điều kiện bình minh/hoàng hôn đều có thể ảnh hưởng đến quan sát.

### 3.3 MyFireWatch

[MyFireWatch](https://myfirewatch.landgate.wa.gov.au/map.html) kết hợp điểm nóng gần đây với nguy cơ cháy, gió, độ xanh thực vật, vùng đã cháy và sét. Dữ liệu thường được làm mới trong khoảng hai đến bốn giờ, tùy thuộc vào vệ tinh.

Tài liệu của hệ thống cảnh báo rằng:

- điểm nóng có thể là nguồn nhiệt công nghiệp;
- đám cháy nhỏ, mát hoặc bị che bởi mây, khói, tán cây có thể bị bỏ sót;
- sai số vị trí có thể khoảng 2 km và lên đến 5 km gần rìa ảnh; và
- hệ thống không tự phân biệt cháy rừng với đốt có kiểm soát.

### 3.4 EFFIS

[EFFIS](https://forest-fire.emergency.copernicus.eu/about-effis/technical-background/active-fire-detection) sử dụng phát hiện bất thường nhiệt từ NASA FIRMS. Hệ thống đã áp dụng bộ lọc dựa trên tri thức, xem xét lớp phủ đất xung quanh, khoảng cách tới bề mặt đô thị hoặc nhân tạo và mức tin cậy của sản phẩm nguồn.

Điều này làm tăng ngưỡng về tính mới: chỉ “thêm lớp phủ đất”, “lọc gần đô thị” hoặc “sử dụng confidence” không còn là đóng góp đủ mạnh nếu không chứng minh được cải thiện bằng thực nghiệm.

## 4. So sánh các nghiên cứu quan trọng

| Tài liệu | Khu vực và dữ liệu | Đóng góp chính | Ý nghĩa đối với đề tài | Vấn đề cần kiểm tra |
|---|---|---|---|---|
| Jones và cộng sự, báo cáo Himawari-8 | NSW và Victoria; Himawari-8 tần suất cao | Thử nghiệm vận hành và chuyển phát hiện tới cơ quan chữa cháy | Chứng minh giám sát điểm nóng tần suất cao đã tồn tại tại Australia | Thiết kế xác thực, báo động giả, độ trễ và nguồn sự kiện tham chiếu |
| Giglio và cộng sự (2016) | MODIS toàn cầu | Thuật toán ngữ cảnh và khung chất lượng Collection 6 | Đường cơ sở vận hành quan trọng | Pixel thô, số lần bay qua hạn chế và ý nghĩa của cờ confidence |
| Schroeder và cộng sự (2014) | VIIRS toàn cầu | Sản phẩm cháy 375 m | Đường cơ sở cho đám cháy nhỏ và độ chính xác vị trí | Tần suất bay qua, lỗi commission và hiệu chỉnh confidence |
| [Zhang và cộng sự (2023)](https://doi.org/10.3390/rs15061541) | Australia; VIIRS và Himawari-8 | Phát hiện thời gian thực đa cảm biến | Nghiên cứu gần nhất với hướng đa cảm biến tại Australia | Căn chỉnh cảm biến, phụ thuộc nhãn, sự kiện chưa thấy và bất định |
| [Zhang và cộng sự (2021)](https://doi.org/10.3390/rs13234790) | Miền đông Australia và miền tây Hoa Kỳ; Sentinel-2 | Phân đoạn cháy bằng DCPA+HRNetV2 | Cho thấy deep learning tại Australia không còn mới | Nhãn bán thủ công, mây/revisit, rò rỉ sự kiện và chuyển miền |
| [Singh và cộng sự (2025)](https://doi.org/10.1007/s11069-025-07163-w) | Wolgan Valley, NSW; Landsat-8 và chỉ số phổ | Phân loại bằng SVM | Đường cơ sở địa phương hữu ích | Chỉ một khu vực và không phù hợp giám sát liên tục |
| [Rad (2024)](https://proceedings.mlr.press/v222/rad24a.html) | Bắc Mỹ; ảnh đa phổ | Phát hiện bằng vision transformer | Chứng minh transformer không tự tạo ra tính mới | Chuyển miền, độ trễ và độ tin cậy được hiệu chỉnh |
| [Barco và cộng sự (2024)](https://arxiv.org/abs/2405.20093) | Các sự kiện tại châu Âu | Học tự giám sát theo chuỗi thời gian | Gợi ý giảm phụ thuộc vào nhãn | Tiền ấn phẩm, chuyển sang Australia và calibration |
| Sen2Fire và [TS-SatFire](https://arxiv.org/abs/2412.11555) | Bộ dữ liệu quốc tế | Chuẩn hóa tác vụ phát hiện và chuỗi thời gian | Hữu ích cho thiết kế benchmark hoặc pretraining | Dịch chuyển phân phối so với vận hành tại Australia |
| [Phan và cộng sự (2022)](https://doi.org/10.1016/j.eswa.2022.117007) | Luồng sự kiện thời gian thực | Giải thích ngữ nghĩa | Cho thấy giải thích trong phát hiện cháy đã tồn tại | Tính trung thực, ổn định và khả năng áp dụng cho lỗi vệ tinh |
| [Kondylatos và cộng sự (2024)](https://doi.org/10.1016/j.scitotenv.2024.173273) | Tổng quan toàn cầu | Tổng hợp dữ liệu và phương pháp phát hiện cháy đang hoạt động | Bản đồ chính cho truy vết tài liệu | Cần đọc toàn văn và lần theo trích dẫn |

Nghiên cứu Sentinel-2 năm 2021 báo cáo IoU khoảng 70–72% ở hai vùng thử nghiệm. Con số này cần được đọc cùng với cách tạo nhãn, cách chia dữ liệu và giới hạn revisit; nó không tự chứng minh hiệu quả vận hành.

[FireCluster](https://www.sciencedirect.com/science/article/pii/S2666017226000611) đã kết hợp MODIS, VIIRS, Landsat-8 và Himawari-8 để nhận dạng sự kiện cháy tại Trung Quốc. Vì vậy, “hợp nhất đa nguồn” nói chung không còn là một tuyên bố mới đủ cụ thể.

## 5. Các phát hiện xuyên suốt tài liệu

### 5.1 Sự bổ trợ giữa cảm biến đã được biết rõ

- MODIS có chuỗi quan sát lâu dài nhưng độ phân giải tương đối thô.
- VIIRS 375 m nhạy hơn với điểm nóng nhỏ.
- Himawari-8 cung cấp quan sát thường xuyên nhưng pixel thô hơn.
- Sentinel-2 và Landsat có thông tin không gian/phổ tốt nhưng revisit và mây hạn chế giám sát liên tục.

Câu hỏi nghiên cứu phải kiểm tra một thiết kế nhận biết cảm biến (*sensor-aware design*) cụ thể, thay vì chỉ tuyên bố kết hợp cảm biến.

### 5.2 Nhãn là rủi ro khoa học trung tâm

Sự đồng thuận giữa hai sản phẩm vệ tinh không tương đương với xác nhận một đám cháy thật. Nếu dùng MODIS hoặc VIIRS làm nhãn, mô hình có thể học lại lỗi bỏ sót, báo động giả và giới hạn độ phân giải của chính sản phẩm đó.

Ranh giới cháy cuối cùng cho biết nơi đã cháy, nhưng không nhất thiết cho biết vị trí ngọn lửa đang hoạt động tại từng thời điểm vệ tinh quan sát. Thiết kế nhãn phải mô tả rõ:

- nguồn sự kiện tham chiếu;
- dung sai không gian và thời gian;
- cách xử lý đốt có kiểm soát và nhiệt công nghiệp;
- cách tạo mẫu âm; và
- mức bất định của nhãn.

### 5.3 Chia dữ liệu ngẫu nhiên có thể thổi phồng kết quả

Pixel lân cận, ảnh cùng thời điểm hoặc nhiều quan sát của cùng một đám cháy có thể xuất hiện ở cả train và test. Nghiên cứu hướng tới triển khai cần giữ lại toàn bộ sự kiện cháy (*held-out event*), giai đoạn tương lai và, nếu đủ dữ liệu, một tiểu vùng riêng biệt.

### 5.4 Chỉ số accuracy thông thường chưa đủ

Accuracy, ROC-AUC hoặc IoU không trực tiếp đo:

- gánh nặng báo động giả;
- số đám cháy nhỏ bị bỏ sót;
- độ trễ phát hiện;
- độ tin cậy của xác suất;
- hiệu quả theo cảm biến, mùa hoặc khu vực; và
- hành vi khi dữ liệu bị thiếu hay bị che khuất.

Các chỉ số nên bao gồm precision, recall, F1, PR-AUC, số báo động giả theo diện tích/thời gian, độ trễ khi đo được, Brier score, đường calibration và expected calibration error.

### 5.5 Confidence và lời giải thích phải được đánh giá

Cờ confidence của sản phẩm, softmax score của mạng nơ-ron và xác suất đã hiệu chỉnh là ba khái niệm khác nhau. Tương tự, một bản đồ attention hoặc SHAP trông hợp lý chưa chứng minh lời giải thích ổn định hay trung thực.

Lời giải thích nên được kiểm tra giữa các fold, sự kiện, mùa và vùng; đồng thời liên hệ với vật lý cảm biến hoặc cơ chế báo động giả đã biết.

## 6. Các hạn chế phương pháp lặp lại

### L1. Đánh đổi độ phân giải không gian–thời gian

Vệ tinh địa tĩnh có tần suất cao nhưng dễ bỏ sót đám cháy nhỏ do pixel thô. Vệ tinh quỹ đạo cực có chi tiết tốt hơn nhưng chỉ đi qua một số thời điểm. Mây, khói, góc nhìn, bão hòa và nhiệt nền làm vấn đề phức tạp hơn.

### L2. Nhãn và sản phẩm tham chiếu không hoàn hảo

Nhãn thủ công đắt và chủ quan. Nhãn từ sản phẩm vệ tinh có thể chuyển lỗi của sản phẩm sang mô hình. Cần phân biệt “khớp với sản phẩm tham chiếu” và “phát hiện một đám cháy đã được xác minh”.

### L3. Xác thực chưa chứng minh khả năng tổng quát hóa

Chia ngẫu nhiên theo patch hoặc pixel dễ gây rò rỉ. Cần xác thực theo sự kiện, thời gian tương lai và địa lý.

### L4. Chỉ số mô hình tách rời chi phí vận hành

Báo động từ công nghiệp, đất trống nóng, mép mây, sun glint và bất thường nhiệt khác đều quan trọng đối với vận hành. Sai số vị trí cũng phải được đưa vào thiết kế ghép sự kiện.

### L5. Confidence chưa được hiệu chỉnh nhất quán

Ít nghiên cứu được sàng lọc báo cáo đồng thời calibration curve, Brier score, expected calibration error và hiệu quả dưới distribution shift.

### L6. Lời giải thích hiếm khi được xác thực

Giải thích cần được kiểm tra tính ổn định và độ trung thực, không chỉ trình bày hình ảnh minh họa.

## 7. Ba khoảng trống nghiên cứu ứng viên

### Khoảng trống A — Khuyến nghị: giám sát đa cảm biến đáng tin cậy

> Mặc dù hệ thống vận hành và nghiên cứu đã kết hợp quan sát từ vệ tinh quỹ đạo cực và địa tĩnh, bằng chứng được rà soát hiện chưa cho thấy rõ một đánh giá tại Australia đồng thời kiểm tra calibration, tổng quát hóa theo sự kiện/thời gian, cơ chế báo động giả, độ bền khi thiếu quan sát và độ ổn định của lời giải thích.

Câu hỏi nghiên cứu dự kiến:

> Liệu mô hình không gian–thời gian nhận biết cảm biến có cải thiện độ tin cậy của confidence trong DEA Hotspots cho một tiểu vùng NSW so với confidence vận hành và các baseline phi nơ-ron mạnh, dưới kiểm định theo sự kiện giữ lại và giai đoạn tương lai hay không?

### Khoảng trống B — Phương án an toàn hơn: kiểm toán độ tin cậy và calibration

So sánh confidence vận hành, logistic regression và mô hình cây dưới cách chia theo sự kiện/thời gian. Tập trung vào calibration và taxonomy báo động giả thay vì ưu tiên kiến trúc phức tạp.

Câu hỏi:

> Các chỉ báo confidence hiện tại của DEA đáng tin cậy đến mức nào giữa các cảm biến, thuật toán, mùa, sự kiện và tiểu vùng NSW; và calibration theo ngữ cảnh có cải thiện tính hữu ích ra quyết định hay không?

### Khoảng trống C — Rủi ro cao hơn: thích ứng thời gian tiết kiệm nhãn

Học tự giám sát trên quan sát Australia chưa gán nhãn, sau đó kiểm tra hiệu quả và calibration khi chỉ có ít sự kiện được xác minh.

Câu hỏi:

> Biểu diễn thời gian tự giám sát có giảm nhu cầu về sự kiện gán nhãn mà vẫn duy trì calibration và chuyển giao địa lý tại Australia hay không?

## 8. Hướng NSW được khuyến nghị

### Tiêu đề làm việc

**Độ tin cậy đáng tin cậy cho điểm nóng cháy đa nguồn và giám sát cháy đang hoạt động: Nghiên cứu trường hợp tại NSW**

NSW là lựa chọn hợp lý ban đầu vì:

- phù hợp với gợi ý của TS Arnick;
- đã có nghiên cứu tại Wolgan Valley và miền đông Australia;
- có [NSW NPWS Fire History](https://data.nsw.gov.au/data/dataset/fire-history-wildfires-and-prescribed-burns-1e8b6);
- có chương trình [Fire Extent and Severity Mapping](https://www.environment.nsw.gov.au/topics/animals-and-plants/native-vegetation/landcover-science/fire-extent-and-severity-maps);
- mùa cháy 2019–20 cung cấp nhiều trường hợp quan trọng; và
- có thể thu hẹp thành Greater Blue Mountains/Wolgan Valley, South Coast hoặc một tiểu vùng theo bioregion.

Điều này không chứng minh NSW luôn là bang “dễ cháy nhất”. Nó cho thấy NSW hiện là nghiên cứu trường hợp khả thi về dữ liệu, mức liên quan, tài liệu trước đó và bối cảnh vận hành.

## 9. Thí nghiệm khả thi tối thiểu

1. Chọn một tiểu vùng NSW sau khi kiểm toán số sự kiện và độ đầy đủ dữ liệu.
2. Định nghĩa chính xác một mục tiêu phát hiện hoặc giám sát.
3. Sử dụng DEA Hotspots cùng metadata về cảm biến, thời gian, confidence và accuracy.
4. Xây dựng nguồn sự kiện tham chiếu độc lập và ghi rõ bất định.
5. Thiết lập baseline từ confidence vận hành, logistic regression và mô hình cây.
6. Chỉ thêm một mô hình thời gian hoặc theo sự kiện nếu dữ liệu hỗ trợ.
7. Giữ lại toàn bộ sự kiện và một giai đoạn tương lai cho test.
8. Báo cáo hiệu quả phát hiện, báo động giả và calibration.
9. Phân tích lỗi theo cảm biến, thuật toán và bối cảnh môi trường.
10. Kiểm tra độ ổn định lời giải thích.

Mô hình đồ thị nên là tùy chọn. Chỉ sử dụng khi có đồ thị hợp lý—ví dụ quan hệ cảm biến–sự kiện, lân cận ô không gian hoặc cụm sự kiện biến đổi theo thời gian—và chứng minh được giá trị vượt baseline đơn giản.

## 10. Rủi ro khả thi chính

| Rủi ro | Tại sao quan trọng | Giảm thiểu sớm |
|---|---|---|
| Không có tham chiếu cháy đang hoạt động độc lập | Không thể dùng sự đồng thuận sản phẩm để chứng minh cháy thật | Kiểm toán Fire History/FESM và hỏi Arnick về nguồn chính xác hơn sau khi có bằng chứng |
| Ranh giới cuối cùng thiếu vị trí ngọn lửa theo thời gian | Ghép không gian có thể tạo nhãn sai | Dùng cửa sổ thời gian minh bạch và ghi lại bất định nhãn |
| Quá ít sự kiện xác minh | Mô hình phức tạp và kiểm tra chuyển miền không đáng tin | Giảm khu vực hoặc độ phức tạp; ưu tiên audit |
| Đốt có kiểm soát và nhiệt công nghiệp | Có thể bị gán nhãn sai | Xây dựng taxonomy sự kiện và báo động giả |
| Sai lệch cảm biến và thời gian | Hợp nhất có thể tạo lỗi căn chỉnh | Phân tích độ nhạy theo dung sai không gian/thời gian |
| Giới hạn học kỳ | Data engineering có thể chiếm toàn bộ dự án | Xem audit calibration là đóng góp tối thiểu khả thi |

## 11. Câu hỏi dành cho TS Arnick

Chỉ nên hỏi sau khi hoàn tất kiểm toán dữ liệu công khai:

1. “Active-fire monitoring” trong đề tài chỉ bao gồm phát hiện lặp lại hiện tại hay có cả dự báo rất ngắn hạn?
2. Fire History/FESM có đủ độc lập và chính xác về thời gian để dùng cho xác thực không?
3. Nếu không, thầy có biết nguồn sự kiện cháy đang hoạt động đã xác minh hoặc kho incident lịch sử nào giải quyết đúng trường còn thiếu không?
4. NSW có phù hợp không, và nên ưu tiên tiểu vùng hoặc mùa cháy nào?
5. Thầy ưu tiên đóng góp phương pháp mới hay đánh giá trustworthy AI chặt chẽ?
6. Nếu nhãn độc lập không đủ, kiểm toán calibration và độ tin cậy có được xem là đóng góp tối thiểu phù hợp không?

## 12. Trình tự đọc được khuyến nghị

### Giai đoạn 1 — Hiểu bài toán vận hành

1. Báo cáo dự án Himawari-8 tại Australia.
2. Tài liệu DEA Hotspots, MyFireWatch và EFFIS.

### Giai đoạn 2 — Nắm thuật toán nền tảng

3. Giglio và cộng sự (2016), MODIS Collection 6.
4. Schroeder và cộng sự (2014), VIIRS 375 m.

### Giai đoạn 3 — Tập trung vào Australia

5. Zhang và cộng sự (2023), VIIRS–Himawari-8.
6. Zhang và cộng sự (2021), Sentinel-2 deep learning.
7. Singh và cộng sự (2025), nghiên cứu NSW.

### Giai đoạn 4 — Phương pháp và dữ liệu mới

8. Rad (2024), vision transformer.
9. Barco và cộng sự (2024), self-supervised temporal learning.
10. Sen2Fire và TS-SatFire.

### Giai đoạn 5 — Độ tin cậy và giải thích

11. Phan và cộng sự (2022), giải thích ngữ nghĩa thời gian thực.
12. Kondylatos và cộng sự (2024), bài tổng quan để mở rộng truy vết trích dẫn.

## 13. Thuật ngữ Anh–Việt

| Thuật ngữ tiếng Anh | Cách dùng tiếng Việt trong tài liệu | Ghi chú |
|---|---|---|
| Active fire | Cháy đang hoạt động | Khác với vùng đã cháy hoặc nguy cơ cháy |
| Active-fire monitoring | Giám sát cháy đang hoạt động | Theo dõi lặp lại, không đồng nghĩa dự báo lan truyền |
| Hotspot / thermal anomaly | Điểm nóng / bất thường nhiệt | Không tự chứng minh cháy thực vật |
| Fire-spread modelling | Mô phỏng lan truyền đám cháy | Nằm ngoài phạm vi |
| Burned-area mapping | Lập bản đồ vùng đã cháy | Tác vụ hồi cứu khác với active-fire detection |
| Confidence | Mức tin cậy / chỉ báo confidence | Không mặc nhiên là xác suất đã calibration |
| Probability calibration | Hiệu chỉnh xác suất | Mức độ xác suất dự báo khớp tần suất thực tế |
| False positive / commission error | Dương tính giả / lỗi phát hiện thừa | Cần nhãn âm đáng tin cậy để xác nhận |
| False negative / omission error | Âm tính giả / lỗi bỏ sót | Có thể do mây, khói, pixel, revisit hoặc thuật toán |
| Event-based validation | Xác thực theo sự kiện | Giữ toàn bộ một đám cháy ngoài tập huấn luyện |
| Chronological holdout | Giữ lại giai đoạn tương lai | Kiểm tra tổng quát hóa theo thời gian |
| Distribution shift | Dịch chuyển phân phối | Thay đổi theo vùng, mùa, cảm biến hoặc sự kiện |
| Explainability | Khả năng giải thích | Cần kiểm tra ổn định và trung thực |
| Multi-sensor fusion | Hợp nhất đa cảm biến | Bản thân việc kết hợp nguồn không đủ tính mới |
| Self-supervised learning | Học tự giám sát | Tận dụng dữ liệu chưa gán nhãn |
| Reference label / ground truth | Nhãn tham chiếu / dữ liệu chuẩn | “Ground truth” trong viễn thám thường vẫn có bất định |

## Kết luận

Hướng nghiên cứu mạnh nhất không phải là tạo thêm một bản đồ điểm nóng hoặc áp dụng một kiến trúc thời thượng. Đóng góp nên xoay quanh câu hỏi khoa học và vận hành rõ ràng: **mức tin cậy của bằng chứng điểm nóng đa cảm biến tại NSW là bao nhiêu, khi nào nó thất bại, và liệu một mô hình nhận biết cảm biến có cải thiện calibration và khả năng tổng quát hóa dưới cách kiểm định thực tế hay không?**

Trước khi cố định mô hình, cần hoàn tất kiểm toán nguồn nhãn, xác nhận định nghĩa “monitoring” với TS Arnick và kiểm chứng khoảng trống qua toàn văn cùng truy vết trích dẫn.
