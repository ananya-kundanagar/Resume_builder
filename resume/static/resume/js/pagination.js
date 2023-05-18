function slide(id){
	var dots = document.getElementsByName("page");
	for (let index = 0; index < dots.length; index++) {
		if(dots[index].id == id){
			console.log(dots[index].id);
			dots[index].classList.add('active')
			moveSlide(index)
		}else{
			dots[index].classList.remove('active')
		}
	}
}

function moveSlide(i){
	var element = document.getElementsByClassName("slide")[0];
	var margin = 378 * i;
	element.style.marginLeft = '-'+margin+'px';
}

function newForm(){
	var element = document.getElementsByClassName("slide")[0];
	var nSlides = document.getElementsByClassName("slide").length - 1;
	var margin = 378 * nSlides;
	element.style.marginLeft = '-'+margin+'px';
}


function newSkill(){
	var element = document.getElementsByClassName("skill-container")[0];
	element.style.marginTop = 0;
}