
/**
 * Input: ub_input, ub_rslt, n_repeat, orig_data_width
 *        pool_stride_h, pool_stride_w
 * Local: ub_meas iter_i, iter_j, loop_marker_i, loop_marker_j
 *        v_template
 *
 * Temp: temp0, temp1
 */
lr_loop_unified_block:

    SUB.s64 @sp, @sp, #24
    ST.b64 @ub_meas, [@SP], #4
    ST.b64 @iter_i,  [@SP], #8
    ST.b64 @iter_j,  [@SP], #12
    ST.b64 @loop_marker_i,  [@SP], #16
    ST.b64 @loop_marker_j, [@sp], #20
    ST.b64 @v_template, [@sp], #24

    MOV @temp0, #0xFFFF
    MOV @temp1, #0xFFFF
    SHL.u64 @temp0, #16
    ADD.u64 @temp0, @temp0, @temp1
    MOVEMASK MASK[0], @temp0
    MOVEMASK MASK[1], @temp0

    /* move to ub_meas to the right place */
    MOV @temp0, @orig_data_width
    SHL.u64 @temp0, #4
    ADD.s64 @ub_meas, @ub_input, @temp0

    /* copy the first element to result for ease of loop */
    MOV @temp0, @pool_stride_w
    SUB.s64 @temp0, @temp0, 1
    SHL.b64 @temp0, #4              // gap between transfers
    MOV @temp1, @temp0
    SHL.b64 @temp1, #16
    MOV @temp0, #1
    ADD.s64 @temp1, @temp0          // # of contig burst
    MOV @temp0, @n_repeat
    SHL.b64 @temp0, @temp, #3       // # of burst, n_repeat*block_size( 8 )
    SHL.b64 @temp1, #12
    ADD.s64 @temp1, @temp1, @temp0
    SHL.b64 @temp, #4               // smmu_id = 0
    MOV_UB_TO_UB [@ub_rslt], [@ub_meas], #temp1, #0, #0
   
    MOV @v_template, @n_repeat          // n_repeat
    SHL.b64 @v_template, #16
    MOV @temp1, @pool_stride_w 
    SHL.b64 @temp1, #3
    ADD.s64 @v_template, @v_template, @temp1 // stride between repeat, for Xm
    SHL.b64 @v_template, #8
    MOV @temp1, #1
    SHL.b64 @temp1, #3
    ADD.s64 @v_template, @v_template, @temp1 // stride between repeat, for Xn
    SHL.b64 @v_template, #8 
    Add.s64 @v_template, @v_template, @temp1 // stride between repeat, for Xd
    SHL.b64 @v_template, #8
    ADD.s64 @v_template, @v_template, @pool_stride_w
    SHL.b64 @v_template, #8
    MOV @temp1, #1
    ADD.s64 @v_template, @v_template, @temp1
    SHL.b64 @v_template, #8
    ADD.s64 @v_template, @v_template, @temp1

    MOV @iter_i, @pad_top
    MOV @loop_marker_i, PC

        MOV @iter_j, @pad_l
        MOV @loop_marker_j, PC

            VMAX.f16 [@ub_rslt], [@ub_rslt], [@ub_meas], @v_template, MASK
            MOV @temp0, #32
            ADD.s64 @ub_meas, @ub_meas, @temp0 // post-update ub_meas

            MOV @temp0, #1
            ADD.s64 @iter_j, @iter_j, @temp0
        CMP.GE.s64 @iter_j, @win_w
        JUMPC #7
        MOV @temp0, PC 
        SUB.s64 @temp0, @loop_marker_j, @temp0
        SHR.s64 @temp0, #2
        MOV @temp1, #5
        SUB.s64 @temp0, @temp0, @temp1
        JUMP @temp0
             
        MOV @temp0, #32   
        MUL.s64 @temp0, @temp0, @win_w
        SUB.s64 @ub_meas, @ub_meas, @temp0
        MOV @temp0, #32
        MUL.s64 @temp0, @temp0, @orig_data_width
        ADD.s64 @ub_meas, @ub_meas, @temp0

        MOV @temp0, #1
        ADD.s64 @iter_im, @iter_i, @temp0
        SUB.s64 @temp0, @win_h, @pad_bot
    CMP.GE.s64 @iter_i, @temp0
    JUMPC #7
    MOV @temp0, PC 
    SUB.s64 @temp0, @loop_marker_i, @temp0
    SHR.s64 @temp0, #2
    MOV @temp1, #5
    SUB.s64 @temp0, @temp0, @temp1
    JUMP @temp0

    LD.b64 @ub_meas, [@SP], #4
    LD.b64 @iter_i,  [@SP], #8
    LD.b64 @iter_j,  [@SP], #12
    LD.b64 @loop_marker_i,  [@SP], #16
    LD.b64 @loop_marker_j, [@sp], #20
    LD.b64 @v_template, [@sp], #24
    ADD.s64 @sp, @sp, #24
    RET

/* Input: win_h, win_w, ub_input, ub_rslt
 *        pad_l, pad_r, pad_top, pad_bot
 *        orig_data_w
 * Local: iter_i, iter_j, loop_begin_i, loop_begin_j, ub_meas
 *
 *
 * Temp: @temp0, @temp1
 */
lr_pool_diverged_block:

    /* Save Local Registers */
    SUB.s64 @SP, @SP, #20
    ST.b64 @iter_i, [@SP], #4
    ST.b64 @iter_j, [@SP], #8
    ST.b64 @loop_begin_i, [@SP], #12
    ST.b64 @loop_begin_j, [@SP], #16
    ST.b64 @ub_meas, [@SP], #20

    /* enable only the first block, and no divergence inside
     * a single block
     */
    MOV @temp #0
    MOVEMASK MASK[1], @temp
    MOV @temp #0xFFFF
    MOVEMASK MASK[0], @temp
    
    /* Move the first element to ub_dest, for ease of the loop
     */
    MOV @ub_meas, @orig_data_w
    SHL.u64 @ub_meas, #4
    MUL.s64 @ub_meas, @pad_top 
    MOV @temp0, @pad_l
    SHL.s64 @temp0, #4
    ADD.s64 @ub_meas, @ub_meas, @temp0
    ADD.s64 @ub_meas, @ub_meas, @ub_input
    MOV @temp1, #1
    SHL.u64 @temp1, #12
    ADD.s64 @temp1, @temp1, #1
    SHL.u64 @temp1, #4
    MOV_UB_TO_UB [@ub_rslt], [@temp0], temp1, #0, #0 

    MOV @iter_i, @pad_top
    MOV @loop_begin_i, PC

        MOV @iter_j, @pad_l
        MOV @loop_begin_j, PC
                 
            MOV @temp0, #1 
            SHL.u64 @temp, #56
            VMAX.f16 [@ub_rslt], [@ub_rslt], [@ub_meas], @temp0, MASK
            MOV @temp0, #32      
            ADD.s64 @ub_meas, @ub_meas, @temp0 // post update ub_meas

            MOV @temp0, #1
            ADD.s64 @iter_j, @temp0 
        
        SUB.s64 @temp0, @win_w, @pad_r
        CMP.GE.s64 @iter_j, @temp0
        JUMPC #7
        MOV @temp0, PC
        SUB.s64 @temp0, @loop_begin_j, @temp0
        SHR.s64 @temp0, #2
        MOV @temp1, #5
        SUB.s64 @temp0, @temp0, @temp1
        JUMP @temp0

        MOV @temp0, #32
        SUB.s64 @temp1, @win_w, @pad_l
        SUB.s64 @temp1, @temp1, @pad_r
        MUL.s64 @temp0, @temp0, @temp1 
        SUB.s64 @ub_meas, @ub_meas, @temp0  // back to begin of the line
        MOV @temp0, #16
        MUL.s64 @temp0, @orig_data_w, @temp0 
        ADD.s64 @ub_meas, @ub_meas, @temp0  // point to the next line

        MOV @temp0, #1 
        ADD.s64 @iter_i, @iter_i, @temp0

    SUB.s64 @temp0, @win_h, @pad_bot
    CMP.GE.s64 @iter_i, @temp0
    JUMPC #7
    MOV @temp0, PC
    SUB.s64 @temp0, @loop_begin_i, @temp0
    SHR.s64 @temp0, #2
    MOV.s64 @temp1, #5
    SUB.s64 @temp0, @temp0, @temp1 
    JUMP @temp0

    /* Restore Local Registers */
    LD.b64 @iter_i, [@SP], #4
    LD.b64 @iter_j, [@SP], #8
    LD.b64 @loop_begin_i, [@SP], #12
    LD.b64 @loop_begin_j, [@SP], #16
    LD.b64 @ub_meas, [@SP], #20
    ADD.s64 @SP, @SP, #20
    RET
