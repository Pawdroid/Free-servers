# Hướng dẫn cấu hình ứng dụng

Hãy chọn ứng dụng trước rồi kiểm tra định dạng đầu vào. Với mỗi ngôn ngữ, liên kết GitHub và Cloudflare của dự án cung cấp cùng một danh sách nút đăng ký URI/Base64 thông thường; đây không phải hồ sơ Clash/Mihomo YAML hoặc sing-box JSON gốc sẵn dùng.

Giữ URL đăng ký riêng tư và thông tin xác thực trên thiết bị của bạn. Không gửi chúng đến các trang chuyển đổi công khai. Nếu cần định dạng khác, hãy lấy hồ sơ tương thích từ nhà cung cấp hoặc tự chuẩn bị trên máy theo tài liệu cấu hình chính thức của ứng dụng đích.

[v2rayN](#v2rayn)
[Clash Verge Rev](#clash-verge-rev)
[Hiddify](#hiddify)
[Clash Party](#clash-party)
[FlClash](#flclash)
[Karing](#karing)
[Throne](#throne)
[Surge Mac](#surge)
[Quantumult X](#quantumult-x)
[sing-box for Apple platforms](#sing-box)
[v2rayNG](#v2rayng)
[Clash Meta for Android](#clash-meta-android)
[Surfboard](#surfboard)
[NekoBox for Android](#nekobox-android)
[Shadowrocket](#shadowrocket)
[Stash](#stash)
[Loon](#loon)
[Egern](#egern)
[Streisand](#streisand)
[Potatso](#potatso)
[OpenClash](#openclash)
[PassWall2 / PassWall](#passwall)
[Nikki](#nikki)
[HomeProxy](#homeproxy)

<a id="v2rayn"></a>

## v2rayN

**Định dạng nhập:** URI / Base64

### Thiết lập nhanh

1. Thêm URL nút được hỗ trợ hoặc đăng ký URI/Base64 thông thường trong phần đăng ký/hồ sơ của ứng dụng. Làm mới đăng ký và kiểm tra các nút mong muốn đã xuất hiện.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [中文]](https://github.com/2dust/v2rayN/wiki/Description-of-some-ui)


<a id="clash-verge-rev"></a>

## Clash Verge Rev

**Định dạng nhập:** Clash / Mihomo YAML

### Thiết lập nhanh

1. Chuẩn bị hồ sơ YAML đầy đủ, tương thích với Clash/Mihomo. Nhập dưới dạng hồ sơ cục bộ hoặc từ xa, cập nhật rồi chọn hồ sơ đó. Đăng ký thông thường ở trên không phải hồ sơ YAML đầy đủ.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [中文]](https://www.clashverge.dev/guide/quickstart.html)


<a id="hiddify"></a>

## Hiddify

**Định dạng nhập:** URI / Base64 · Clash YAML · sing-box JSON

Ứng dụng này đọc được nhiều định dạng, nhưng với đăng ký của dự án hãy dùng cách nhập URI/Base64 thông thường. Hồ sơ JSON gốc và YAML vẫn có yêu cầu riêng.

### Thiết lập nhanh

1. Thêm URL nút được hỗ trợ hoặc đăng ký URI/Base64 thông thường trong phần đăng ký/hồ sơ của ứng dụng. Làm mới đăng ký và kiểm tra các nút mong muốn đã xuất hiện.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [English]](https://hiddify.com/app/How-to-use-Hiddify-app/)


<a id="clash-party"></a>

## Clash Party

**Định dạng nhập:** Clash / Mihomo YAML

### Thiết lập nhanh

1. Chuẩn bị hồ sơ YAML đầy đủ, tương thích với Clash/Mihomo. Nhập dưới dạng hồ sơ cục bộ hoặc từ xa, cập nhật rồi chọn hồ sơ đó. Đăng ký thông thường ở trên không phải hồ sơ YAML đầy đủ.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [中文]](https://clashparty.org/docs/handson)


<a id="flclash"></a>

## FlClash

**Định dạng nhập:** Clash / Mihomo YAML

Hướng dẫn người dùng chính thức còn hạn chế; hãy dùng các bước thiết lập ngắn và tài liệu định dạng chính thức đã xác minh bên dưới.

### Thiết lập nhanh

1. Chuẩn bị hồ sơ YAML đầy đủ, tương thích với Clash/Mihomo. Nhập dưới dạng hồ sơ cục bộ hoặc từ xa, cập nhật rồi chọn hồ sơ đó. Đăng ký thông thường ở trên không phải hồ sơ YAML đầy đủ.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

Hướng dẫn ngắn này trình bày định dạng đầu vào đã xác minh và quy trình cơ bản. Tài liệu kỹ thuật được liên kết không phải hướng dẫn người dùng từng bước; tên các mục trên giao diện có thể thay đổi theo phiên bản.

- [Tài liệu kỹ thuật [English]](https://github.com/chen08209/FlClash#usage)

<a id="karing"></a>

## Karing

**Định dạng nhập:** URI / Base64 · Clash YAML · sing-box JSON

Ứng dụng này đọc được nhiều định dạng, nhưng với đăng ký của dự án hãy dùng cách nhập URI/Base64 thông thường. Hồ sơ JSON gốc và YAML vẫn có yêu cầu riêng.

### Thiết lập nhanh

1. Thêm URL nút được hỗ trợ hoặc đăng ký URI/Base64 thông thường trong phần đăng ký/hồ sơ của ứng dụng. Làm mới đăng ký và kiểm tra các nút mong muốn đã xuất hiện.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [English]](https://karing.app/en/quickstart)


<a id="throne"></a>

## Throne

**Định dạng nhập:** URI / Base64 · sing-box JSON · Clash YAML proxies

Khi nhập đăng ký, ứng dụng trích xuất các nút được hỗ trợ; không mặc định rằng quy tắc và các thiết lập khác của hồ sơ gốc sẽ được giữ lại.

### Thiết lập nhanh

1. Thêm URL nút được hỗ trợ hoặc đăng ký URI/Base64 thông thường trong phần đăng ký/hồ sơ của ứng dụng. Làm mới đăng ký và kiểm tra các nút mong muốn đã xuất hiện.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [English]](https://throneproj.github.io/get_started/configuration/)


<a id="surge"></a>

## Surge Mac

**Định dạng nhập:** Surge INI / Managed Profile

Dùng cấu hình Surge hoặc URL cấu hình được quản lý. Không coi đăng ký V2Ray thông thường là cấu hình Surge đầy đủ.

### Thiết lập nhanh

1. Chuẩn bị hồ sơ đầy đủ theo định dạng nêu trên. Nhập tệp cục bộ hoặc URL hồ sơ từ xa mà ứng dụng hỗ trợ, cập nhật rồi chọn hồ sơ đó. Không mặc định rằng đăng ký nút thông thường và cấu hình của ứng dụng khác có thể thay thế cho nhau.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [English]](https://manual.nssurge.com/getting-started/quick-start.html)


<a id="quantumult-x"></a>

## Quantumult X

**Định dạng nhập:** Quantumult X / server_remote

Quantumult X sử dụng cấu hình riêng và tài nguyên máy chủ từ xa; cấu hình đầy đủ và tài nguyên nút là hai loại đầu vào khác nhau.

Hướng dẫn người dùng chính thức còn hạn chế; hãy dùng các bước thiết lập ngắn và tài liệu định dạng chính thức đã xác minh bên dưới.

### Thiết lập nhanh

1. Chuẩn bị hồ sơ đầy đủ theo định dạng nêu trên. Nhập tệp cục bộ hoặc URL hồ sơ từ xa mà ứng dụng hỗ trợ, cập nhật rồi chọn hồ sơ đó. Không mặc định rằng đăng ký nút thông thường và cấu hình của ứng dụng khác có thể thay thế cho nhau.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

Hướng dẫn ngắn này trình bày định dạng đầu vào đã xác minh và quy trình cơ bản. Tài liệu kỹ thuật được liên kết không phải hướng dẫn người dùng từng bước; tên các mục trên giao diện có thể thay đổi theo phiên bản.

- [Tài liệu kỹ thuật [中文 / English]](https://github.com/crossutility/Quantumult-X/blob/master/sample.conf)

<a id="sing-box"></a>

## sing-box for Apple platforms

**Định dạng nhập:** sing-box JSON

### Thiết lập nhanh

1. Chuẩn bị hồ sơ sing-box JSON đầy đủ phù hợp với phiên bản lõi của ứng dụng. Thêm dưới dạng hồ sơ cục bộ hoặc từ xa rồi cập nhật. Danh sách URL nút hoặc tệp Clash YAML không thể dùng làm sing-box JSON gốc.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [English]](https://sing-box.sagernet.org/clients/general/)


<a id="v2rayng"></a>

## v2rayNG

**Định dạng nhập:** URI / Base64

Hướng dẫn người dùng chính thức còn hạn chế; hãy dùng các bước thiết lập ngắn và tài liệu định dạng chính thức đã xác minh bên dưới.

### Thiết lập nhanh

1. Thêm URL nút được hỗ trợ hoặc đăng ký URI/Base64 thông thường trong phần đăng ký/hồ sơ của ứng dụng. Làm mới đăng ký và kiểm tra các nút mong muốn đã xuất hiện.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

Hướng dẫn ngắn này trình bày định dạng đầu vào đã xác minh và quy trình cơ bản. Tài liệu kỹ thuật được liên kết không phải hướng dẫn người dùng từng bước; tên các mục trên giao diện có thể thay đổi theo phiên bản.

- [Tài liệu kỹ thuật [English]](https://github.com/2dust/v2rayNG/wiki/Mode)

<a id="clash-meta-android"></a>

## Clash Meta for Android

**Định dạng nhập:** Clash / Mihomo YAML

Hướng dẫn người dùng chính thức còn hạn chế; hãy dùng các bước thiết lập ngắn và tài liệu định dạng chính thức đã xác minh bên dưới.

### Thiết lập nhanh

1. Chuẩn bị hồ sơ YAML đầy đủ, tương thích với Clash/Mihomo. Nhập dưới dạng hồ sơ cục bộ hoặc từ xa, cập nhật rồi chọn hồ sơ đó. Đăng ký thông thường ở trên không phải hồ sơ YAML đầy đủ.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

Hướng dẫn ngắn này trình bày định dạng đầu vào đã xác minh và quy trình cơ bản. Tài liệu kỹ thuật được liên kết không phải hướng dẫn người dùng từng bước; tên các mục trên giao diện có thể thay đổi theo phiên bản.

- [Tài liệu kỹ thuật [English]](https://wiki.metacubex.one/en/handbook/syntax/)
- [Tài liệu kỹ thuật [English]](https://github.com/MetaCubeX/ClashMetaForAndroid#automation)

<a id="surfboard"></a>

## Surfboard

**Định dạng nhập:** Surfboard / Surge profile

Dùng cấu hình Surge hoặc URL cấu hình được quản lý. Không coi đăng ký V2Ray thông thường là cấu hình Surge đầy đủ.

Hướng dẫn người dùng chính thức còn hạn chế; hãy dùng các bước thiết lập ngắn và tài liệu định dạng chính thức đã xác minh bên dưới.

### Thiết lập nhanh

1. Chuẩn bị hồ sơ đầy đủ theo định dạng nêu trên. Nhập tệp cục bộ hoặc URL hồ sơ từ xa mà ứng dụng hỗ trợ, cập nhật rồi chọn hồ sơ đó. Không mặc định rằng đăng ký nút thông thường và cấu hình của ứng dụng khác có thể thay thế cho nhau.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

Hướng dẫn ngắn này trình bày định dạng đầu vào đã xác minh và quy trình cơ bản. Tài liệu kỹ thuật được liên kết không phải hướng dẫn người dùng từng bước; tên các mục trên giao diện có thể thay đổi theo phiên bản.

- [Tài liệu kỹ thuật [English]](https://getsurfboard.com/docs/profile-format/overview/)

<a id="nekobox-android"></a>

## NekoBox for Android

**Định dạng nhập:** URI / Base64 · Clash proxies · sing-box outbounds

Khi nhập đăng ký, ứng dụng trích xuất các nút được hỗ trợ; không mặc định rằng quy tắc và các thiết lập khác của hồ sơ gốc sẽ được giữ lại.

### Thiết lập nhanh

1. Thêm URL nút được hỗ trợ hoặc đăng ký URI/Base64 thông thường trong phần đăng ký/hồ sơ của ứng dụng. Làm mới đăng ký và kiểm tra các nút mong muốn đã xuất hiện.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [中文]](https://matsuridayo.github.io/nb4a-configuration/)


<a id="shadowrocket"></a>

## Shadowrocket

**Định dạng nhập:** Shadowrocket subscriptions / profiles

Hướng dẫn người dùng chính thức còn hạn chế; hãy dùng các bước thiết lập ngắn và tài liệu định dạng chính thức đã xác minh bên dưới.

### Thiết lập nhanh

1. Chuẩn bị đăng ký nút hoặc cấu hình nút riêng lẻ mà ứng dụng này hỗ trợ. Thêm bằng cách nhập được mô tả trong tài liệu của ứng dụng, cập nhật đăng ký nếu được hỗ trợ và kiểm tra các nút đã xuất hiện. Danh sách nút và hồ sơ định tuyến đầy đủ là hai loại đầu vào khác nhau.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

- [Thông tin sản phẩm chính thức [English]](https://apps.apple.com/us/app/shadowrocket/id932747118)

<a id="stash"></a>

## Stash

**Định dạng nhập:** Stash / Clash YAML

### Thiết lập nhanh

1. Chuẩn bị hồ sơ YAML đầy đủ, tương thích với Clash/Mihomo. Nhập dưới dạng hồ sơ cục bộ hoặc từ xa, cập nhật rồi chọn hồ sơ đó. Đăng ký thông thường ở trên không phải hồ sơ YAML đầy đủ.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [English]](https://stash.wiki/en/get-started)


<a id="loon"></a>

## Loon

**Định dạng nhập:** URI / Base64 · Loon configuration

Loon sử dụng định dạng cấu hình và đăng ký nút riêng. Kiểm tra từng giao thức và trường dữ liệu, không mặc định tương thích hoàn toàn với Surge hoặc Clash.

### Thiết lập nhanh

1. Thêm URL nút được hỗ trợ hoặc đăng ký URI/Base64 thông thường trong phần đăng ký/hồ sơ của ứng dụng. Làm mới đăng ký và kiểm tra các nút mong muốn đã xuất hiện.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [English]](https://nsloon.app/en/docs/Node/subscription/)


<a id="egern"></a>

## Egern

**Định dạng nhập:** Egern Profile.yaml / proxies YAML

Egern YAML là định dạng hồ sơ riêng, không phải Clash/Mihomo YAML.

Hướng dẫn người dùng chính thức còn hạn chế; hãy dùng các bước thiết lập ngắn và tài liệu định dạng chính thức đã xác minh bên dưới.

### Thiết lập nhanh

1. Chuẩn bị hồ sơ đầy đủ theo định dạng nêu trên. Nhập tệp cục bộ hoặc URL hồ sơ từ xa mà ứng dụng hỗ trợ, cập nhật rồi chọn hồ sơ đó. Không mặc định rằng đăng ký nút thông thường và cấu hình của ứng dụng khác có thể thay thế cho nhau.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

Hướng dẫn ngắn này trình bày định dạng đầu vào đã xác minh và quy trình cơ bản. Tài liệu kỹ thuật được liên kết không phải hướng dẫn người dùng từng bước; tên các mục trên giao diện có thể thay đổi theo phiên bản.

- [Tài liệu kỹ thuật [English]](https://egernapp.com/docs/configuration/policy_groups/)

<a id="streisand"></a>

## Streisand

**Định dạng nhập:** Supported node configurations

Hướng dẫn người dùng chính thức còn hạn chế; hãy dùng các bước thiết lập ngắn và tài liệu định dạng chính thức đã xác minh bên dưới.

### Thiết lập nhanh

1. Chuẩn bị đăng ký nút hoặc cấu hình nút riêng lẻ mà ứng dụng này hỗ trợ. Thêm bằng cách nhập được mô tả trong tài liệu của ứng dụng, cập nhật đăng ký nếu được hỗ trợ và kiểm tra các nút đã xuất hiện. Danh sách nút và hồ sơ định tuyến đầy đủ là hai loại đầu vào khác nhau.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

- [Thông tin sản phẩm chính thức [English]](https://streisand.pages.dev/)

<a id="potatso"></a>

## Potatso

**Định dạng nhập:** Mihomo / Clash YAML · supported node links

Hướng dẫn người dùng chính thức còn hạn chế; hãy dùng các bước thiết lập ngắn và tài liệu định dạng chính thức đã xác minh bên dưới.

### Thiết lập nhanh

1. Chuẩn bị hồ sơ YAML đầy đủ, tương thích với Clash/Mihomo. Nhập dưới dạng hồ sơ cục bộ hoặc từ xa, cập nhật rồi chọn hồ sơ đó. Đăng ký thông thường ở trên không phải hồ sơ YAML đầy đủ.
2. Nếu hồ sơ cho phép lựa chọn, hãy chọn nút hoặc nhóm proxy, sau đó bật chế độ proxy/VPN theo tài liệu của ứng dụng. Chỉ cấp quyền VPN của hệ điều hành cho ứng dụng chính thức đã cài đặt. Kiểm tra truy cập thực tế sau khi kết nối.
3. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

- [Thông tin sản phẩm chính thức [English]](https://potatso.com/)

<a id="openclash"></a>

## OpenClash

**Định dạng nhập:** Clash / Mihomo YAML

### Thiết lập nhanh

1. Trước khi cài đặt, kiểm tra firmware, kiến trúc CPU, các gói phụ thuộc và bộ nhớ khả dụng. Sao lưu cấu hình bộ định tuyến và duy trì kết nối quản trị hoạt động. Chỉ nhập đăng ký/hồ sơ được hỗ trợ, cập nhật, chọn nút hoặc nhóm đầu ra rồi bật plugin theo hướng dẫn chính thức.
2. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [中文]](https://github.com/vernesong/OpenClash#快速开始)


<a id="passwall"></a>

## PassWall2 / PassWall

**Định dạng nhập:** Supported node URI subscriptions

Khi nhập đăng ký, ứng dụng trích xuất các nút được hỗ trợ; không mặc định rằng quy tắc và các thiết lập khác của hồ sơ gốc sẽ được giữ lại.

Hướng dẫn người dùng chính thức còn hạn chế; hãy dùng các bước thiết lập ngắn và tài liệu định dạng chính thức đã xác minh bên dưới.

### Thiết lập nhanh

1. Trước khi cài đặt, kiểm tra firmware, kiến trúc CPU, các gói phụ thuộc và bộ nhớ khả dụng. Sao lưu cấu hình bộ định tuyến và duy trì kết nối quản trị hoạt động. Chỉ nhập đăng ký/hồ sơ được hỗ trợ, cập nhật, chọn nút hoặc nhóm đầu ra rồi bật plugin theo hướng dẫn chính thức.
2. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

Hướng dẫn ngắn này trình bày định dạng đầu vào đã xác minh và quy trình cơ bản. Tài liệu kỹ thuật được liên kết không phải hướng dẫn người dùng từng bước; tên các mục trên giao diện có thể thay đổi theo phiên bản.

- [Tài liệu kỹ thuật [English]](https://github.com/Openwrt-Passwall/openwrt-passwall2)
- [Tài liệu kỹ thuật [English]](https://github.com/Openwrt-Passwall/openwrt-passwall)

<a id="nikki"></a>

## Nikki

**Định dạng nhập:** Mihomo YAML: proxies / proxy-providers

### Thiết lập nhanh

1. Trước khi cài đặt, kiểm tra firmware, kiến trúc CPU, các gói phụ thuộc và bộ nhớ khả dụng. Sao lưu cấu hình bộ định tuyến và duy trì kết nối quản trị hoạt động. Chỉ nhập đăng ký/hồ sơ được hỗ trợ, cập nhật, chọn nút hoặc nhóm đầu ra rồi bật plugin theo hướng dẫn chính thức.
2. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

[Hướng dẫn chính thức [中文]](https://github.com/nikkinikki-org/OpenWrt-nikki/wiki)


<a id="homeproxy"></a>

## HomeProxy

**Định dạng nhập:** HomeProxy node subscriptions

HomeProxy quản lý nút và đăng ký qua giao diện riêng. Kiểm tra các định dạng mà phiên bản đã cài đặt hỗ trợ; việc sử dụng sing-box bên trong không có nghĩa là có thể nhập một hồ sơ sing-box JSON đầy đủ bất kỳ.

Hướng dẫn người dùng chính thức còn hạn chế; hãy dùng các bước thiết lập ngắn và tài liệu định dạng chính thức đã xác minh bên dưới.

### Thiết lập nhanh

1. Trước khi cài đặt, kiểm tra firmware, kiến trúc CPU, các gói phụ thuộc và bộ nhớ khả dụng. Sao lưu cấu hình bộ định tuyến và duy trì kết nối quản trị hoạt động. Chỉ nhập đăng ký/hồ sơ được hỗ trợ, cập nhật, chọn nút hoặc nhóm đầu ra rồi bật plugin theo hướng dẫn chính thức.
2. Nếu cập nhật thất bại, kiểm tra URL, mạng và lỗi HTTP. Nếu phân tích dữ liệu thất bại, kiểm tra định dạng và phiên bản lõi. Nếu nhập thành công nhưng không kết nối được, hãy làm mới và thử nút khác được hỗ trợ, rồi xem nhật ký lỗi của ứng dụng. Cập nhật hoặc kiểm tra độ trễ thành công không đảm bảo khả năng sử dụng hay độ an toàn.

Kiểm tra các giao thức được hỗ trợ và phiên bản lõi đã cài đặt; nhập nút không đảm bảo toàn bộ quy tắc, thiết lập DNS hoặc trường nâng cao sẽ được giữ lại.

Hướng dẫn ngắn này trình bày định dạng đầu vào đã xác minh và quy trình cơ bản. Tài liệu kỹ thuật được liên kết không phải hướng dẫn người dùng từng bước; tên các mục trên giao diện có thể thay đổi theo phiên bản.

- [Tài liệu kỹ thuật [English]](https://github.com/immortalwrt/homeproxy)
