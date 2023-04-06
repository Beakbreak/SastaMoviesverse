import classes from './ContentSlider.module.scss';
import MoviePoster from './MoviePoster';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Slider from 'react-slick';
function SampleNextArrow(props) {
    const { className, style, onClick } = props;
    return (
        <div
            className={`${classes.arrow} ${classes.right}`}
            onClick={onClick}
        />
    );
}

function SamplePrevArrow(props) {
    const { className, style, onClick } = props;
    return (
        <div
            className={`${classes.arrow} ${classes.left}`}
            onClick={onClick}
        />
    );
}
const ContentSlider = (props) => {
    const settings = {
        dots: false,
        infinite: true,
        speed: 500,
        slidesToShow: 6,
        slidesToScroll: 3,
        nextArrow: <SampleNextArrow />,
        prevArrow: <SamplePrevArrow />,
        variableWidth: true,
        adaptiveHeight: true
    };

    return (<>
        <div >
            <h2 className={classes.movType}>{props.title}<p className={classes.viewall}>View All<div className={classes["arrow-container"]}>
                <div className={classes.arrowt}></div>
                <div className={classes.arrowt}></div>
                <div className={classes.arrowt}></div>
            </div></p></h2>
            <Slider {...settings} className={classes.slider}>
                <div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div></Slider>
        </div >
    </>);
}
export default ContentSlider;


