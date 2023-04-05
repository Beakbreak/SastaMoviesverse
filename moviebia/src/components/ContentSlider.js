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
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 6,
        slidesToScroll: 3,
        nextArrow: <SampleNextArrow />,
        prevArrow: <SamplePrevArrow />,
    };

    return (<>
        <div >
            <h2 className={classes.movType}>{props.title}</h2>
            <Slider {...settings} className={classes.slider}>
                <div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div></Slider>
        </div >
    </>);
}
export default ContentSlider;


