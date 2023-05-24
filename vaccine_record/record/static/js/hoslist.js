function showHospitals() {
	// Lấy giá trị của quận được chọn
	var appointmentfor = document.getElementById("appointmentfor").value;

	// Khai báo danh sách bệnh viện theo từng quận
	var hospitals = {
		"quandong": ["Bệnh viện Hữu Nghị Việt Đức", "Bệnh viện Nhi đồng 1", "Bệnh viện Từ Dũ"],
		"quanphunhuan": ["Bệnh viện An Sinh", "Bệnh viện Hoàn Mỹ Sài Gòn", "Bệnh viện Tim Tâm Đức"],
		"quanbinhthanh": ["Bệnh viện Ung Bướu TP.HCM", "Bệnh viện Gia Định", "Bệnh viện Bình Thạnh"],
        "quanthuduc": ["Bệnh viện Quân Y 175", "Bệnh viện Phổi Đà Lạt", "Bệnh viện Đa Khoa Thủ Đức"],
        "quan5": ["Bệnh viện Nhiệt Đới TP.HCM", "Bệnh viện Chấn thương chỉnh hình", "Bệnh viện 115"],
        "quan10": ["Bệnh viện Đại Học Y Dược", "Bệnh viện Nhi Đồng 2", "Bệnh viện Nhi Tâm Đức"],
        "quan11": ["Bệnh viện Chợ Rẫy 2", "Bệnh viện Truyền Máu Huyết Học", "Bệnh viện Sản Nhi Đa Khoa"],
        "quan12": ["Bệnh viện Đa Khoa Hồng Đức", "Bệnh viện Xuyên Á", "Bệnh viện Đa Khoa Quốc Tế Hoàn Mỹ"]
    };

// Lấy danh sách bệnh viện tương ứng với quận được chọn
var hospitalList = hospitals[appointmentfor];

// Hiển thị danh sách bệnh viện
var hospitalListDiv = document.getElementById("hospital-list");
hospitalListDiv.innerHTML = "";
if (hospitalList) {
	var list = "<ul>";
	for (var i = 0; i < hospitalList.length; i++) {
		list += "<li>" + hospitalList[i] + "</li>";
	}
	list += "</ul>";
	hospitalListDiv.innerHTML = list;
} else {
	hospitalListDiv.innerHTML = "Không tìm thấy bệnh viện phù hợp với quận đã chọn.";
}
}