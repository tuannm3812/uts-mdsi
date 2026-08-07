# Kịch bản thuyết trình — Buổi họp thứ Sáu 7/8 với Dr Arnick (Bản tiếng Việt)

Bản dịch tiếng Việt của [`week-02-meeting-presentation-script-2026-08-07.md`](week-02-meeting-presentation-script-2026-08-07.md), dùng để chuẩn bị/luyện tập — **buổi họp thực tế vẫn diễn ra bằng tiếng Anh**, nên các câu "Nói:" bên dưới nên được nói lại bằng tiếng Anh khi họp (bản gốc tiếng Anh có sẵn để tham khảo trực tiếp nếu cần). Đây là gợi ý nội dung, không phải kịch bản đọc nguyên văn — nói theo cách của mình.

**Nguyên văn lời của Dr Arnick được giữ nguyên bằng tiếng Anh** (đánh dấu *"Nguyên văn"*), kèm bản dịch tiếng Việt ngay bên dưới để dễ hiểu. Đọc lại đúng lời của ông trước mỗi đề xuất là cách nhanh để xác nhận đã hiểu đúng ý, đồng thời cho thấy mọi đề xuất đều dựa trên điều ông thực sự nói, không phải suy đoán. Nguồn đầy đủ: [`communications/from-arnick-2026-08-05-direction-correction.md`](../communications/from-arnick-2026-08-05-direction-correction.md) và [`communications/from-arnick-2026-07-29-scope-clarification.md`](../communications/from-arnick-2026-07-29-scope-clarification.md).

**Thời lượng dự kiến:** 30–45 phút. Cần 7 quyết định trước khi kết thúc (Mục 4 bên dưới) — đó mới là mục tiêu thực sự của buổi họp, phần còn lại chỉ là bối cảnh để đi đến đó nhanh hơn. Có bảng tick đi kèm ([`week-02-decision-checklist-2026-08-07.md`](week-02-decision-checklist-2026-08-07.md), bản PDF) để đánh dấu trực tiếp trong lúc họp.

---

## 0. Mở đầu (30 giây)

> "Thanks for making time. Quick structure for today: I'll recap what's changed since the 3 August brief, confirm I understood your redirect correctly, show you the public notebooks quickly, then I've got seven things I'd like your decision on so I can start building next week. Should take 30–40 minutes."

*(Cảm ơn thầy đã dành thời gian. Cấu trúc hôm nay: em sẽ tóm tắt những gì thay đổi từ bản brief ngày 3/8, xác nhận em hiểu đúng hướng điều chỉnh của thầy, cho thầy xem nhanh hai notebook công khai, sau đó có 7 điều em muốn xin quyết định của thầy để bắt đầu xây dựng vào tuần tới. Khoảng 30–40 phút.)*

---

## 1. Tóm tắt từ ngày 3/8 (2 phút)

> "Since the brief, I extended the reliability pilot to use NPWS Fire History instead of NSW RFS, since RFS's license wasn't actually confirmed for redistribution. That let me publish the whole thing as a reproducible public Kaggle pipeline — I'll show you in a second."

*(Từ bản brief, em đã mở rộng thí điểm kiểm định độ tin cậy, chuyển sang dùng NPWS Fire History thay vì NSW RFS, vì giấy phép của RFS chưa thực sự được xác nhận cho việc tái phân phối. Nhờ đó em đã công bố toàn bộ pipeline dưới dạng công khai, có thể tái lập trên Kaggle — em sẽ cho thầy xem ngay sau đây.)*

**Phát hiện chính cần nói rõ ràng:**

> "The headline result: neither reference is actually good enough on its own. NSW RFS — narrow, incident-level records — only matched 17.1% of hotspots even with sensor-buffering. NPWS — broad, whole-of-season fire-complex boundaries — matched 97.12%. That jump isn't sensor improvement, it's scale. Two mega-complexes, Kerry Ridge and Gospers Mountain, account for about 98% of every match in NPWS. So the real lesson isn't 'NPWS is better,' it's that reference-data granularity dominates the result more than anything about the sensors themselves."

*(Kết quả chính: không nguồn tham chiếu nào thực sự đủ tốt một mình. NSW RFS — dữ liệu hẹp, theo từng sự cố — chỉ khớp 17.1% số điểm nóng dù đã áp dụng vùng đệm theo cảm biến. NPWS — ranh giới rộng, theo cả mùa cháy — khớp 97.12%. Bước nhảy đó không phải do cảm biến tốt hơn, mà do quy mô dữ liệu tham chiếu. Hai đám cháy siêu lớn, Kerry Ridge và Gospers Mountain, chiếm khoảng 98% tổng số điểm khớp trong NPWS. Vậy bài học thực sự không phải "NPWS tốt hơn", mà là độ chi tiết của dữ liệu tham chiếu chi phối kết quả nhiều hơn bất cứ điều gì liên quan đến bản thân các cảm biến.)*

*(Đây là phát hiện dễ gây nhiều thảo luận nhất — nên dành đủ thời gian, đừng vội lướt qua.)*

---

## 2. Xác nhận hướng điều chỉnh (2 phút)

**Nguyên văn (5/8):** *"But this project is not about the reliability auditing of those existing platforms and methodology for hotspot monitoring."* ... *"what I was thinking is that, we get hotspot datasets like time series of fire hotspots from sensors like MODIS (FIRMS)... create a dataset of all fire hotspots timeseries from for example 2000-25 for training the model."* ... *"then build multimodal spatiotemporal transformer (time series model) with different modalities coming from MODIS, weather, vegetation/land cover etc and cross-attention for fusion."*

*(Dịch: "Nhưng dự án này không phải về việc kiểm định độ tin cậy của các nền tảng và phương pháp giám sát điểm nóng hiện có." ... "Điều thầy nghĩ là mình lấy dữ liệu chuỗi thời gian điểm nóng từ các cảm biến như MODIS (FIRMS)... tạo một bộ dữ liệu chuỗi thời gian điểm nóng cháy, ví dụ từ 2000-2025, để huấn luyện mô hình." ... "sau đó xây dựng transformer không-thời gian đa phương thức, kết hợp các dữ liệu từ MODIS, thời tiết, thảm thực vật/lớp phủ đất... bằng cross-attention.")*

**Nói:**
> "I want to make sure I understood your reply correctly before I show you anything else. You said the reliability audit isn't the project — it's groundwork. The actual target, in your words, is a MODIS FIRMS hotspot time series from 2000 to 2025, checked for confidence, fused with weather and land-cover data, feeding a multimodal spatiotemporal transformer with cross-attention. And you wanted one prediction output, not both — either occurrence probability with explanation, or 1-to-7-day forecasting. Is that a fair summary?"

*(Em muốn chắc chắn đã hiểu đúng phản hồi của thầy trước khi cho thầy xem gì khác. Thầy nói việc kiểm định độ tin cậy không phải là dự án — đó chỉ là nền tảng. Mục tiêu thực sự, theo lời thầy, là một chuỗi thời gian điểm nóng MODIS FIRMS từ 2000 đến 2025, đã được kiểm tra độ tin cậy, kết hợp với dữ liệu thời tiết và lớp phủ đất, đưa vào một transformer không-thời gian đa phương thức dùng cross-attention. Và thầy muốn một đầu ra dự đoán duy nhất, không phải cả hai — hoặc xác suất xảy ra cháy kèm giải thích, hoặc dự báo 1-7 ngày. Em tóm tắt vậy có đúng không ạ?)*

*(Dừng lại chờ thầy xác nhận trước khi tiếp tục — đây là nền tảng cho mọi thứ phía sau.)*

---

## 3. Trình bày notebook (3–5 phút, chia sẻ màn hình)

Mở cả hai link (đã gửi trước qua Teams):
- Notebook EDA: https://www.kaggle.com/code/tuannm3812/nsw-active-fire-eda
- Notebook khớp độ tin cậy: https://www.kaggle.com/code/tuannm3812/nsw-active-fire-reliability-pilot

**Trình bày theo thứ tự:**
1. Notebook EDA, Mục 5 ("Key EDA Takeaways") — bảng độ lệch diện tích, chỉ ra sự áp đảo của Gospers Mountain/Kerry Ridge.
2. Notebook độ tin cậy, Mục 3 ("Results") — hai con số chính 77.25%/97.12%.
3. Notebook độ tin cậy, Mục 4 ("Event Concentration") — biểu đồ cột, ~98% tập trung vào hai sự kiện.
4. Notebook độ tin cậy, cuối bài — ghi chú "Project Context and Roadmap", gắn thí điểm này trực tiếp vào hướng dự báo.

> "Both notebooks are public and reproducible — dataset plus two separate kernels, so either one can be re-run independently on Kaggle's free tier."

*(Cả hai notebook đều công khai và có thể tái lập — một dataset cộng hai kernel riêng biệt, mỗi cái có thể chạy lại độc lập trên gói miễn phí của Kaggle.)*

---

## 4. Bảy quyết định (20–25 phút — phần trọng tâm của buổi họp)

Trình bày mỗi mục theo kiểu "đây là điều nhóm em đề xuất, thầy thấy ổn không hay muốn điều chỉnh" — không phải câu hỏi mở. Nhanh hơn để chốt, và cho thấy hướng đi không xuất phát từ con số 0. Tick vào bảng [decision checklist](week-02-decision-checklist-2026-08-07.md) khi thầy trả lời từng mục.

### 4.1 Khung thời gian dự báo
**Nguyên văn (5/8):** *"prediction hotspots with showing confidence and uncertainty level based on those time series auxiliary data for next for example 1-7 days ahead (this can change based on final data and possibility of the model)."*

*(Dịch: "dự đoán điểm nóng kèm mức độ tin cậy và bất định, dựa trên dữ liệu phụ trợ chuỗi thời gian, cho ví dụ 1-7 ngày tới (có thể thay đổi tùy theo dữ liệu cuối cùng và khả năng của mô hình).")*

**Nói:**
> "You said 1-to-7 days, with room to change based on the data. We'd recommend keeping it as a multi-horizon output across the full range, rather than one fixed day — the literature we found shows uncertainty grows measurably with horizon, worth showing explicitly. Does that work?"

*(Thầy nói 1-7 ngày, có thể điều chỉnh tùy dữ liệu. Nhóm em đề xuất giữ đầu ra đa khung thời gian trên toàn bộ khoảng đó, thay vì chỉ một ngày cố định — tài liệu nhóm em tìm được cho thấy độ bất định tăng rõ rệt theo khung thời gian, đáng để thể hiện rõ. Thầy thấy vậy có ổn không?)*

### 4.2 Vùng nghiên cứu điển hình
**Nguyên văn (29/7):** *"you can select a specific study region - for example, a state in Australia such as NSW - to build and analyse your model... You could also look at which regions or states in Australia are more fire-prone and use one of those as your case study."*

*(Dịch: "em có thể chọn một vùng nghiên cứu cụ thể - ví dụ, một bang của Úc như NSW - để xây dựng và phân tích mô hình... Em cũng có thể xem vùng/bang nào của Úc dễ cháy hơn và dùng vùng đó làm case study.")*

**Nói:**
> "Back on 29 July you said NSW broadly, or a fire-prone subregion within it. This week's pilot found a real reason to be careful about which subregion: if we stay in the exact Blue Mountains pilot footprint, two events dominate everything and we can't validate properly. We'd recommend either widening to all of NSW, or a different fire-prone subregion with more distinct events. Do you have a preference, or should we choose based on where the data actually supports proper validation?"

*(Ngày 29/7 thầy nói NSW nói chung, hoặc một tiểu vùng dễ cháy trong đó. Thí điểm tuần này tìm ra lý do thực sự để cẩn trọng khi chọn tiểu vùng: nếu giữ nguyên phạm vi thí điểm Blue Mountains, hai sự kiện sẽ chi phối toàn bộ dữ liệu và không thể kiểm định đúng cách. Nhóm em đề xuất hoặc mở rộng ra toàn NSW, hoặc chọn một tiểu vùng dễ cháy khác có nhiều sự kiện tách biệt hơn. Thầy có vùng nào ưu tiên không, hay để nhóm em chọn dựa trên nơi dữ liệu thực sự hỗ trợ kiểm định tốt?)*

### 4.3 Dữ liệu phụ trợ
**Nguyên văn (5/8):** *"auxiliary data to this with additional variables like weather (rainfall, temperature, wind, humidity, etc), land cover and vegetation condition, etc. for each hotspot location and records."*

*(Dịch: "dữ liệu phụ trợ với các biến bổ sung như thời tiết (lượng mưa, nhiệt độ, gió, độ ẩm, v.v.), lớp phủ đất và tình trạng thảm thực vật, v.v. cho từng vị trí và bản ghi điểm nóng.")*

**Nói:**
> "For weather, we'd use SILO — free, gridded, daily, goes back to 1889, covers the full FIRMS window with no gaps. For land cover, DEA Land Cover — same agency as DEA Hotspots, which you already pointed us to. Unless you've got a preferred or prepared dataset, we'd start there."

*(Về thời tiết, nhóm em dùng SILO — miễn phí, dạng lưới, theo ngày, có từ 1889, phủ toàn bộ khoảng thời gian FIRMS mà không thiếu dữ liệu. Về lớp phủ đất, dùng DEA Land Cover — cùng cơ quan với DEA Hotspots mà thầy đã chỉ trước đó. Trừ khi thầy có bộ dữ liệu ưu tiên hoặc đã chuẩn bị sẵn, nhóm em sẽ bắt đầu từ đó.)*

*(Nếu thầy hỏi về gió: SILO không có dữ liệu này — đã kiểm tra trực tiếp danh sách biến của họ. Nói thẳng: "gió cần nguồn khác, BOM hoặc ERA5, nhóm em chưa tìm nguồn cho việc này.")*

### 4.4 Bộ dữ liệu Digital Atlas
**Nguyên văn (5/8):** *"or burned datasets like (https://digital.atlas.gov.au/datasets/524e2962bd8b4968b8df9f9774345926/about)."*

*(Dịch: "hoặc các bộ dữ liệu vùng cháy như (đường link).")*

**Nói:**
> "You linked the Digital Atlas 'Bushfire Historical Extents' dataset — we checked it. CC BY 4.0, no licensing issue. But its NSW records trace back to the same NSW Parks and Wildlife source as NPWS, which we're already using — so it's very likely the same underlying data re-aggregated nationally, not an independent check. We'd treat it as useful mainly if the region ever crosses a state border. Does that match what you had in mind for it?"

*(Thầy có gửi link bộ dữ liệu Digital Atlas "Bushfire Historical Extents" — nhóm em đã kiểm tra. Giấy phép CC BY 4.0, không vướng vấn đề bản quyền. Nhưng dữ liệu NSW trong đó truy về cùng nguồn NSW Parks and Wildlife như NPWS mà nhóm em đang dùng — nên rất có thể đây là cùng một dữ liệu gốc, chỉ được tổng hợp lại ở cấp quốc gia, không phải một kiểm chứng độc lập. Nhóm em sẽ coi nó hữu ích chủ yếu khi vùng nghiên cứu vượt ranh giới bang. Điều đó có đúng với ý thầy khi gửi link này không?)*

### 4.5 Hạ tầng tính toán
Không có câu nào của thầy đề cập trực tiếp đến mục này — đây là câu hỏi thực sự mở, không dựa trên trích dẫn cụ thể.

**Nói:**
> "We'll default to Kaggle's free tier for prototyping and baselines. If the full 2000-to-2025 multimodal training run needs more than that, is there UTS compute or cloud credits available as a fallback? Better to know now than mid-semester."

*(Nhóm em sẽ mặc định dùng gói miễn phí của Kaggle để thử nghiệm và làm baseline. Nếu việc huấn luyện đầy đủ mô hình đa phương thức từ 2000-2025 cần nhiều hơn thế, liệu có hạ tầng tính toán của UTS hoặc credit cloud nào dự phòng không? Biết trước bây giờ vẫn tốt hơn là giữa học kỳ mới phát hiện ra.)*

### 4.6 Định hướng đóng góp khoa học
**Nguyên văn (5/8):** *"check work pipeline and do a bit of search how this looks like and how to add innovation to this and then see how to build methodology, data and models."* ... *"Because of timeframe of the research subject, can not add more complexity to the project."*

*(Dịch: "kiểm tra quy trình làm việc và tìm hiểu thêm xem việc này trông như thế nào, làm sao thêm được yếu tố đổi mới, rồi xem cách xây dựng phương pháp, dữ liệu và mô hình." ... "Vì thời hạn của môn nghiên cứu, không thể thêm độ phức tạp cho dự án.")*

**Nói:**
> "You asked us to find where the innovation actually is, within a tight timeframe. Our recommendation is 'reliability-aware forecasting' — propagating the label-confidence work from Phase 1 into the model's own uncertainty estimate, plus split-complex validation, now backed by three independent literature findings. We think that's a real contribution in its own right, not just scaffolding around the transformer, and it doesn't add complexity — it reuses what's already built. Does that framing work for how you want the semester allocated?"

*(Thầy yêu cầu nhóm em tìm ra điểm đổi mới thực sự, trong một khung thời gian eo hẹp. Đề xuất của nhóm em là "dự báo có nhận thức về độ tin cậy" — lan truyền công việc đánh giá độ tin cậy nhãn từ Giai đoạn 1 vào chính ước lượng bất định của mô hình, cộng với kiểm định split-complex, hiện đã được ba phát hiện độc lập trong tài liệu khoa học ủng hộ. Nhóm em cho rằng đây là một đóng góp thực sự, không chỉ là phần phụ trợ quanh transformer, và nó không làm tăng độ phức tạp — mà tận dụng lại những gì đã xây dựng. Định hướng này có phù hợp với cách thầy muốn phân bổ thời gian học kỳ không?)*

### 4.7 Khớp chéo cảm biến — một khoảng trống mới phát hiện khi đọc lại tin nhắn của thầy
**Nguyên văn (5/8):** *"this can be done based on your review through fire records from NSW for exmaple, or corss-sesnor matching and validation like with other sensor like VIIRS or Himawari, or burned datasets like..."*

*(Dịch: "việc này có thể làm dựa trên đánh giá của em qua dữ liệu cháy từ NSW chẳng hạn, hoặc khớp chéo và kiểm định với cảm biến khác như VIIRS hay Himawari, hoặc các bộ dữ liệu vùng cháy như...")*

**Nói:**
> "One more thing, going back through your message carefully — you named cross-sensor matching with VIIRS or Himawari as one of three confidence-filtering methods. We've done the other two — NSW fire-record matching and the Digital Atlas check — but cross-sensor agreement itself, checking whether MODIS and VIIRS actually agree with each other at the same place and time, hasn't been done as its own step yet. We'd fold it into the data-foundation work as an explicit task. Wanted to flag it directly rather than let it quietly slip."

*(Một điều nữa, khi đọc lại kỹ tin nhắn của thầy — thầy có nêu việc khớp chéo cảm biến với VIIRS hoặc Himawari là một trong ba phương pháp lọc độ tin cậy. Nhóm em đã làm hai phương pháp còn lại — khớp với dữ liệu cháy NSW và kiểm tra Digital Atlas — nhưng bản thân việc khớp chéo cảm biến, tức kiểm tra xem MODIS và VIIRS có thực sự đồng thuận với nhau tại cùng vị trí và thời điểm hay không, thì chưa được thực hiện như một bước riêng. Nhóm em sẽ đưa việc này vào phần xây dựng nền tảng dữ liệu như một nhiệm vụ rõ ràng. Em muốn nêu trực tiếp thay vì để nó lặng lẽ bị bỏ sót.)*

---

## 5. Kết thúc (1 phút)

> "So to confirm what I'm taking away: [restate his answers to the seven items above]. I'll start on the data-sourcing work next week — full FIRMS history plus weather and land-cover for the confirmed region — and send a short written update once that's underway."

*(Vậy để xác nhận lại những gì em ghi nhận: [nhắc lại câu trả lời của thầy cho 7 mục trên]. Em sẽ bắt đầu công việc thu thập dữ liệu vào tuần tới — toàn bộ lịch sử FIRMS cộng dữ liệu thời tiết và lớp phủ đất cho vùng đã chốt — và gửi một bản cập nhật ngắn khi công việc đang tiến hành.)*

---

## Nếu thầy hỏi điều gì chưa có trong kịch bản

- **"Sao không dùng NSW RFS vì nó chính xác hơn?"** → Giấy phép chưa từng được xác nhận cho việc tái phân phối (D-005) — đó mới là lý do thực sự chuyển sang NPWS, không phải vì sở thích.
- **"Em tin vào con số 97.12% đến mức nào?"** → Đã được kiểm chứng độc lập nhiều lần trong quá trình làm việc, bao gồm cả việc tính lại phân bổ theo từng sự kiện trực tiếp từ code khớp dữ liệu so với dữ liệu thô, không chỉ đọc lại từ notebook.
- **"Cái gì thực sự đã xong, cái gì chưa bắt đầu?"** → Trả lời thẳng: Giai đoạn 1 (kiểm định độ tin cậy) đã xong và đã công bố. Giai đoạn 3 (xây dựng nền tảng dữ liệu đa thập kỷ thực sự, T-033) **chưa** bắt đầu — nói thẳng điều này thay vì ngụ ý đã tiến xa hơn thực tế.
