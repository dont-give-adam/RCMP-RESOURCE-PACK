#version 330
#extension GL_ARB_separate_shader_objects : require

uniform sampler2D InSampler;

layout(location = 0) in vec2 texCoord;
layout(location = 0) out vec4 fragColor;


#define STRENGTH 1.0


void main() {
    vec4 original_pixel_color = texture(InSampler,texCoord);
    vec4 current_pixel_color = original_pixel_color;

    float largest = max(current_pixel_color.r,current_pixel_color.y);
    largest = max(largest,current_pixel_color.b);

    current_pixel_color.rgb = vec3(largest);



        current_pixel_color.rgb *= 0.5;

        current_pixel_color.rgb = vec3(smoothstep(0.0,1.0,current_pixel_color.rgb));


    // finalized output: set the output pixel to the calculated value
    current_pixel_color = vec4(vec3(current_pixel_color),1.0);

    fragColor = mix(original_pixel_color,current_pixel_color,STRENGTH);

}